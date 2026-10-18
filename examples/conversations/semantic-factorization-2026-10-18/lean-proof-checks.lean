-- Executed in the public Lean 4.30.0 core-library playground on 2026-10-18.
-- No sorry/admit placeholders are used.
-- This checks the stated arithmetic and toy-contract obligations only.

theorem nat_add_zero (n : Nat) : n + 0 = n := by
  simp

theorem identity_age_mapping_preserves_nonneg (source dest : Int)
    (hSource : 0 <= source) (hMap : dest = source) : 0 <= dest := by
  omega

theorem exact_days_to_years (years : Nat) : (365 * years) / 365 = years := by
  omega

theorem naive_units_counterexample :
    Exists fun (p : Int × Int) => 1 <= p.1 && p.2 = 365 * p.1 && p.2 != p.1 := by
  exact ⟨(1, 365), by decide⟩

#print nat_add_zero
#print identity_age_mapping_preserves_nonneg
#print exact_days_to_years
#print naive_units_counterexample
