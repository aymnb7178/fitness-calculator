# Fitness Calculator

A small Python module and command-line tool that estimates **BMI**, **BMR** (Mifflin-St Jeor) and **daily calories (TDEE)**.

> Informational only - **not medical advice**. Written with AI assistance (Claude), reviewed and published by the repository owner.

## Run

```bash
python fitness.py --sex male --age 30 --weight 70 --height 175 --activity moderate
# BMI : 22.9 (normal)
# BMR : 1649 kcal/day
# TDEE: 2556 kcal/day (moderate)

python -m unittest -v        # 6 tests
```

Activity levels: `sedentary`, `light`, `moderate`, `active`, `very_active`. Python 3.8+, no packages needed.

## Formulas

| Value | Formula |
|---|---|
| BMI | kg / m^2, WHO adult categories (<18.5 underweight, <25 normal, <30 overweight, else obese) |
| BMR | 10 x kg + 6.25 x cm - 5 x age + 5 (male) or - 161 (female) |
| TDEE | BMR x activity multiplier (1.2 / 1.375 / 1.55 / 1.725 / 1.9) |

## Verified

- ✅ 6 unit tests: hand-calculated BMI and BMR values, category boundaries, case-insensitive sex, input validation.
- ✅ CLI run with the example above.

## Limits / not built

BMI ignores muscle mass; the equations are population estimates. Body-fat estimate, tracking and a Streamlit interface are **not** implemented.

## Author

Aymen - [github.com/aymnb7178](https://github.com/aymnb7178)
