import unittest

from fitness import ACTIVITY, bmi, bmi_category, bmr, tdee


class TestFitness(unittest.TestCase):
    def test_bmi_known_value(self):
        self.assertAlmostEqual(bmi(70, 175), 22.857, places=3)

    def test_bmi_categories_and_boundaries(self):
        self.assertEqual(bmi_category(18.4), "underweight")
        self.assertEqual(bmi_category(18.5), "normal")
        self.assertEqual(bmi_category(24.9), "normal")
        self.assertEqual(bmi_category(25), "overweight")
        self.assertEqual(bmi_category(30), "obese")

    def test_bmr_mifflin_known_values(self):
        # male: 10*70 + 6.25*175 - 5*30 + 5 = 1648.75
        self.assertAlmostEqual(bmr("male", 30, 70, 175), 1648.75)
        # female: 10*60 + 6.25*165 - 5*25 - 161 = 1345.25
        self.assertAlmostEqual(bmr("female", 25, 60, 165), 1345.25)

    def test_sex_is_case_insensitive(self):
        self.assertEqual(bmr("Male", 30, 70, 175), bmr("male", 30, 70, 175))

    def test_tdee(self):
        self.assertAlmostEqual(tdee(1600, "sedentary"), 1920)
        self.assertEqual(set(ACTIVITY), {"sedentary", "light", "moderate", "active", "very_active"})

    def test_invalid_inputs(self):
        for bad in (lambda: bmi(0, 170), lambda: bmi(70, -1), lambda: bmr("x", 30, 70, 170),
                    lambda: bmr("male", 0, 70, 170), lambda: tdee(1500, "couch")):
            with self.assertRaises(ValueError):
                bad()


if __name__ == "__main__":
    unittest.main()
