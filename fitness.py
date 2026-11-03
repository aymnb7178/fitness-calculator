"""BMI, BMR and daily calorie estimates.

Informational only - NOT medical advice.
Run:  python fitness.py --sex male --age 30 --weight 70 --height 175 --activity moderate
"""
from __future__ import annotations

import argparse

ACTIVITY = {  # standard activity multipliers used with BMR to estimate TDEE
    "sedentary": 1.2,
    "light": 1.375,
    "moderate": 1.55,
    "active": 1.725,
    "very_active": 1.9,
}


def _positive(name: str, value: float) -> None:
    if not isinstance(value, (int, float)) or value <= 0:
        raise ValueError(f"{name} must be a positive number")


def bmi(weight_kg: float, height_cm: float) -> float:
    """Body-mass index = kg / m^2."""
    _positive("weight_kg", weight_kg)
    _positive("height_cm", height_cm)
    m = height_cm / 100.0
    return weight_kg / (m * m)


def bmi_category(value: float) -> str:
    """WHO adult categories."""
    if value < 18.5:
        return "underweight"
    if value < 25:
        return "normal"
    if value < 30:
        return "overweight"
    return "obese"


def bmr(sex: str, age: int, weight_kg: float, height_cm: float) -> float:
    """Basal metabolic rate, Mifflin-St Jeor equation (kcal/day)."""
    _positive("age", age)
    _positive("weight_kg", weight_kg)
    _positive("height_cm", height_cm)
    s = sex.lower()
    if s not in ("male", "female"):
        raise ValueError("sex must be 'male' or 'female'")
    base = 10 * weight_kg + 6.25 * height_cm - 5 * age
    return base + 5 if s == "male" else base - 161


def tdee(bmr_value: float, activity: str) -> float:
    """Total daily energy expenditure = BMR x activity multiplier."""
    if activity not in ACTIVITY:
        raise ValueError(f"activity must be one of {sorted(ACTIVITY)}")
    return bmr_value * ACTIVITY[activity]


def main(argv=None) -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--sex", required=True, choices=["male", "female"])
    ap.add_argument("--age", required=True, type=int)
    ap.add_argument("--weight", required=True, type=float, help="kg")
    ap.add_argument("--height", required=True, type=float, help="cm")
    ap.add_argument("--activity", default="moderate", choices=sorted(ACTIVITY))
    a = ap.parse_args(argv)
    try:
        b = bmi(a.weight, a.height)
        r = bmr(a.sex, a.age, a.weight, a.height)
        t = tdee(r, a.activity)
    except ValueError as e:
        raise SystemExit(f"error: {e}")
    print(f"BMI : {b:.1f} ({bmi_category(b)})")
    print(f"BMR : {r:.0f} kcal/day")
    print(f"TDEE: {t:.0f} kcal/day ({a.activity})")
    print("Estimates only - not medical advice.")


if __name__ == "__main__":
    main()
