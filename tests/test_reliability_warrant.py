import pytest

from inquiry_graph.reliability import (
    MeasurementCertificate,
    TestimonyCertificate as _TestimonyCertificate,
    TestimonyReliabilityModel as _TestimonyReliabilityModel,
)
from inquiry_graph.warrant import (
    EpistemicAction,
    Guarantee,
    MeasurementResultWarrantRegime,
    TestimonyPosteriorWarrantRegime,
    WarrantJudgment,
)


def test_measurement_result_warrants_recording_value_with_uncertainty():
    certificate = MeasurementCertificate(
        id="m1",
        quantity="length",
        value=10.0,
        standard_uncertainty=0.2,
        unit="mm",
        calibration_ref="cal-2026-09",
        measurement_model_ref="linear-ruler-model",
    )
    judgment = WarrantJudgment(
        regime="measurement-result",
        certificate_id=certificate.id,
        action=EpistemicAction("record_measurement_result", "length"),
        guarantee=Guarantee(
            "measurement-result-with-uncertainty",
            "recorded result carries explicit uncertainty and calibration provenance",
        ),
    )
    regime = MeasurementResultWarrantRegime()

    assessment = regime.assess(judgment, certificate)
    decision = regime.derive_license(assessment)

    assert assessment.warranted is True
    assert assessment.value == 10.0
    assert assessment.standard_uncertainty == 0.2
    assert assessment.unit == "mm"
    assert decision.licensed is True


def test_measurement_result_does_not_license_accepting_world_claim():
    certificate = MeasurementCertificate(
        id="m1",
        quantity="length",
        value=10.0,
        standard_uncertainty=0.2,
        unit="mm",
        calibration_ref="cal-2026-09",
    )
    judgment = WarrantJudgment(
        regime="measurement-result",
        certificate_id=certificate.id,
        action=EpistemicAction("accept", "object-length-is-10mm"),
        guarantee=Guarantee(
            "measurement-result-with-uncertainty",
            "measurement result recorded",
        ),
    )
    regime = MeasurementResultWarrantRegime()

    assessment = regime.assess(judgment, certificate)

    assert assessment.warranted is False
    assert "outside" in assessment.reason


def test_measurement_context_assumptions_remain_separate_from_certificate():
    certificate = MeasurementCertificate(
        id="m1",
        quantity="temperature",
        value=20.0,
        standard_uncertainty=0.5,
        unit="degC",
        calibration_ref="thermometer-cal",
    )
    judgment = WarrantJudgment(
        regime="measurement-result",
        certificate_id=certificate.id,
        assumptions={"instrument-within-calibration-period"},
        action=EpistemicAction("record_measurement_result", "temperature"),
        guarantee=Guarantee(
            "measurement-result-with-uncertainty",
            "measurement result recorded",
        ),
    )
    regime = MeasurementResultWarrantRegime()

    assessment = regime.assess(judgment, certificate)
    decision = regime.derive_license(assessment, context_assumptions=())

    assert assessment.warranted is True
    assert decision.licensed is False
    assert decision.unmet_assumptions == frozenset(
        {"instrument-within-calibration-period"}
    )


def test_testimony_model_computes_posterior_for_positive_report():
    reliability = _TestimonyReliabilityModel(
        source_id="witness-1",
        reference_class="weather-reports",
        sensitivity=0.9,
        false_positive_rate=0.1,
    )
    certificate = _TestimonyCertificate(
        id="t1",
        claim="it-rained",
        prior_probability=0.2,
        reliability=reliability,
    )

    assert certificate.report_probability == pytest.approx(0.26)
    assert certificate.posterior_probability == pytest.approx(
        0.18 / 0.26
    )


def test_testimony_regime_warrants_recording_posterior_not_accepting_claim():
    reliability = _TestimonyReliabilityModel(
        source_id="witness-1",
        reference_class="weather-reports",
        sensitivity=0.99,
        false_positive_rate=0.01,
    )
    certificate = _TestimonyCertificate(
        id="t1",
        claim="it-rained",
        prior_probability=0.5,
        reliability=reliability,
    )
    regime = TestimonyPosteriorWarrantRegime()

    record = WarrantJudgment(
        regime="testimony-posterior",
        certificate_id=certificate.id,
        action=EpistemicAction("record_testimonial_posterior", "it-rained"),
        guarantee=Guarantee(
            "testimonial-posterior-under-source-model",
            "posterior follows from declared prior and reliability model",
        ),
    )
    assessment = regime.assess(record, certificate)
    assert assessment.warranted is True
    assert assessment.posterior_probability == pytest.approx(0.99)
    assert assessment.source_id == "witness-1"
    assert assessment.reference_class == "weather-reports"

    accept = WarrantJudgment(
        regime="testimony-posterior",
        certificate_id=certificate.id,
        action=EpistemicAction("accept", "it-rained"),
        guarantee=Guarantee(
            "testimonial-posterior-under-source-model",
            "posterior follows from declared prior and reliability model",
        ),
    )
    accept_assessment = regime.assess(accept, certificate)
    assert accept_assessment.warranted is False


def test_testimony_reliability_is_reference_class_relative():
    first = _TestimonyCertificate(
        id="t-weather",
        claim="it-rained",
        prior_probability=0.5,
        reliability=_TestimonyReliabilityModel(
            source_id="same-source",
            reference_class="weather-reports",
            sensitivity=0.95,
            false_positive_rate=0.05,
        ),
    )
    second = _TestimonyCertificate(
        id="t-medical",
        claim="diagnosis-x",
        prior_probability=0.5,
        reliability=_TestimonyReliabilityModel(
            source_id="same-source",
            reference_class="medical-reports",
            sensitivity=0.6,
            false_positive_rate=0.2,
        ),
    )

    assert first.posterior_probability == pytest.approx(0.95)
    assert second.posterior_probability == pytest.approx(0.75)
    assert first.reliability.source_id == second.reliability.source_id
    assert first.reliability.reference_class != second.reliability.reference_class


def test_testimony_zero_probability_report_is_rejected():
    certificate = _TestimonyCertificate(
        id="t1",
        claim="h",
        prior_probability=0.0,
        reliability=_TestimonyReliabilityModel(
            source_id="s",
            reference_class="r",
            sensitivity=0.0,
            false_positive_rate=0.0,
        ),
    )

    with pytest.raises(ValueError, match="zero probability"):
        _ = certificate.posterior_probability


def test_reliability_certificate_validation():
    with pytest.raises(ValueError, match="standard uncertainty"):
        MeasurementCertificate(
            id="m",
            quantity="x",
            value=1.0,
            standard_uncertainty=-1.0,
            unit="u",
            calibration_ref="c",
        )

    with pytest.raises(ValueError, match="sensitivity"):
        _TestimonyReliabilityModel(
            source_id="s",
            reference_class="r",
            sensitivity=1.1,
            false_positive_rate=0.0,
        )

    with pytest.raises(ValueError, match="reference class"):
        _TestimonyReliabilityModel(
            source_id="s",
            reference_class="",
            sensitivity=0.5,
            false_positive_rate=0.5,
        )
