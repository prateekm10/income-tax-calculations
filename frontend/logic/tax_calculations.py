# =========================================
# tax_calculations.py
# =========================================

def calculate_old_regime_2025(
    salary: float,
    house_property: float,
    other_income: float,
    digital_assets: float,
    ded_80c: float,
    ded_80d: float,
    ded_80ccd: float,
    ded_80g: float,
    ded_other: float
) -> dict:
    """
    Old Regime calculation for FY 2025-26
    """

    # 1. Gross Income (excluding digital assets)
    gross_income_non_digital = salary + house_property + other_income

    # 2. Standard Deduction (₹50k if salary > 0)
    standard_deduction = 50000 if salary > 0 else 0

    # 3. Cap major deductions
    capped_80c = min(ded_80c, 150000)
    capped_80d = min(ded_80d, 50000)
    capped_80ccd = min(ded_80ccd, 50000)

    # 4. Sum all deductions
    total_deductions = (
        standard_deduction +
        capped_80c +
        capped_80d +
        capped_80ccd +
        ded_80g +
        ded_other
    )

    # 5. Taxable Income
    taxable_income = gross_income_non_digital - total_deductions
    if taxable_income < 0:
        taxable_income = 0

    # 6. Slab-based tax (Old Regime)
    slab_tax = 0
    remaining = taxable_income
    slab_breakup = []

    # Slab 1: 0% on 0-2.5L
    slab_1 = min(250000, remaining)
    slab_breakup.append({
        "range": "₹0 - ₹2.5L",
        "amount": slab_1,
        "rate": "0%",
        "tax": 0
    })
    remaining -= slab_1

    # Slab 2: 5% on 2.5-5L
    slab_2_tax = 0
    if remaining > 0:
        slab_2 = min(250000, remaining)
        slab_2_tax = slab_2 * 0.05
        slab_breakup.append({
            "range": "₹2.5L - ₹5L",
            "amount": slab_2,
            "rate": "5%",
            "tax": slab_2_tax
        })
        slab_tax += slab_2_tax
        remaining -= slab_2

    # Slab 3: 20% on 5-10L
    slab_3_tax = 0
    if remaining > 0:
        slab_3 = min(500000, remaining)
        slab_3_tax = slab_3 * 0.20
        slab_breakup.append({
            "range": "₹5L - ₹10L",
            "amount": slab_3,
            "rate": "20%",
            "tax": slab_3_tax
        })
        slab_tax += slab_3_tax
        remaining -= slab_3

    # Slab 4: 30% above 10L
    slab_4_tax = 0
    if remaining > 0:
        slab_4 = remaining
        slab_4_tax = slab_4 * 0.30
        slab_breakup.append({
            "range": "Above ₹10L",
            "amount": slab_4,
            "rate": "30%",
            "tax": slab_4_tax
        })
        slab_tax += slab_4_tax
        remaining -= slab_4

    # 7. Digital Assets @30%
    digital_assets_tax = digital_assets * 0.30

    # 8. Total tax before cess
    total_tax_before_cess = slab_tax + digital_assets_tax

    # 9. Cess @4%
    cess = total_tax_before_cess * 0.04

    # 10. Final total
    total_tax = total_tax_before_cess + cess

    # === NEW: net income after tax ===
    gross_income = salary + house_property + other_income + digital_assets
    net_income_after_tax = gross_income - total_tax

    return {
        "gross_income": gross_income,
        "total_deductions": total_deductions,
        "taxable_income": taxable_income,
        "income_tax": slab_tax,
        "digital_assets_tax": digital_assets_tax,
        "cess": cess,
        "total_tax": total_tax,
        "net_income_after_tax": net_income_after_tax,  # <-- ADDED
        "slab_breakup": slab_breakup,
        "standard_deduction": standard_deduction
    }


def calculate_new_regime_2025(
    salary: float,
    house_property: float,
    other_income: float,
    digital_assets: float
) -> dict:
    """
    New Regime calculation for FY 2025-26
    """

    standard_deduction = 75000 if salary > 0 else 0
    gross_income_non_digital = salary + house_property + other_income
    taxable_income = max(0, gross_income_non_digital - standard_deduction)

    slab_tax = 0
    remaining = taxable_income
    slab_breakup = []

    # Slab 1: 0% on 0-4L
    slab_1 = min(400000, remaining)
    slab_breakup.append({
        "range": "₹0 - ₹4L",
        "amount": slab_1,
        "rate": "0%",
        "tax": 0
    })
    remaining -= slab_1

    # Slab 2: 5% on 4-8L
    slab_2_tax = 0
    if remaining > 0:
        slab_2 = min(400000, remaining)
        slab_2_tax = slab_2 * 0.05
        slab_breakup.append({
            "range": "₹4L - ₹8L",
            "amount": slab_2,
            "rate": "5%",
            "tax": slab_2_tax
        })
        slab_tax += slab_2_tax
        remaining -= slab_2

    # Slab 3: 10% on 8-12L
    slab_3_tax = 0
    if remaining > 0:
        slab_3 = min(400000, remaining)
        slab_3_tax = slab_3 * 0.10
        slab_breakup.append({
            "range": "₹8L - ₹12L",
            "amount": slab_3,
            "rate": "10%",
            "tax": slab_3_tax
        })
        slab_tax += slab_3_tax
        remaining -= slab_3

    # Slab 4: 15% on 12-16L
    slab_4_tax = 0
    if remaining > 0:
        slab_4 = min(400000, remaining)
        slab_4_tax = slab_4 * 0.15
        slab_breakup.append({
            "range": "₹12L - ₹16L",
            "amount": slab_4,
            "rate": "15%",
            "tax": slab_4_tax
        })
        slab_tax += slab_4_tax
        remaining -= slab_4

    # Slab 5: 20% on 16-20L
    slab_5_tax = 0
    if remaining > 0:
        slab_5 = min(400000, remaining)
        slab_5_tax = slab_5 * 0.20
        slab_breakup.append({
            "range": "₹16L - ₹20L",
            "amount": slab_5,
            "rate": "20%",
            "tax": slab_5_tax
        })
        slab_tax += slab_5_tax
        remaining -= slab_5

    # Slab 6: 25% on 20-24L
    slab_6_tax = 0
    if remaining > 0:
        slab_6 = min(400000, remaining)
        slab_6_tax = slab_6 * 0.25
        slab_breakup.append({
            "range": "₹20L - ₹24L",
            "amount": slab_6,
            "rate": "25%",
            "tax": slab_6_tax
        })
        slab_tax += slab_6_tax
        remaining -= slab_6

    # Slab 7: 30% above 24L
    slab_7_tax = 0
    if remaining > 0:
        slab_7 = remaining
        slab_7_tax = slab_7 * 0.30
        slab_breakup.append({
            "range": "Above ₹24L",
            "amount": slab_7,
            "rate": "30%",
            "tax": slab_7_tax
        })
        slab_tax += slab_7_tax
        remaining -= slab_7

    # Digital Assets @30%
    digital_assets_tax = digital_assets * 0.30

    total_tax_before_rebate = slab_tax + digital_assets_tax

    # Rebate if taxable_income <= 12L
    rebate = 0
    if taxable_income <= 1200000:
        rebate = min(total_tax_before_rebate, 60000)

    tax_after_rebate = total_tax_before_rebate - rebate
    if tax_after_rebate < 0:
        tax_after_rebate = 0

    # Cess @4%
    cess = tax_after_rebate * 0.04
    total_tax = tax_after_rebate + cess

    # === NEW: net income after tax ===
    gross_income = salary + house_property + other_income + digital_assets
    net_income_after_tax = gross_income - total_tax

    return {
        "gross_income": gross_income,
        "standard_deduction": standard_deduction,
        "taxable_income": taxable_income,
        "income_tax": slab_tax,
        "digital_assets_tax": digital_assets_tax,
        "rebate": rebate,
        "cess": cess,
        "total_tax": total_tax,
        "net_income_after_tax": net_income_after_tax,  # <-- ADDED
        "slab_breakup": slab_breakup
    }
