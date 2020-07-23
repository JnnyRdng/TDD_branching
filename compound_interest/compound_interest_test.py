import unittest

from compound_interest import CompoundInterest


class CompoundInterestTest(unittest.TestCase):

    # Tests
    # Should have principal property
    def test_has_principal_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(100, compound.principal)

    # Should have percent property
    def test_has_percent_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(0.1, compound.percent)

    def test_has_years_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(20, compound.years)

    def test_has_frequency_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(12, compound.frequency)

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_call_get_interest_function(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertIsNotNone(compound.get_interest())

    def test_given_100_10_20(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(732.81, compound.get_interest())

    # Should return 181.94 given 100 principal, 6 percent, 10 years
    def test_given_100_6_10(self):
        compound = CompoundInterest(100, 6, 10)
        self.assertEqual(181.94, compound.get_interest())

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years
    def test_given_100000_5_8(self):
        compound = CompoundInterest(100000, 5, 8)
        self.assertEqual(149058.55, compound.get_interest())

    # Should return 0.00 given 0 principal, 10 percent, 1 year
    def test_given_0_10_1(self):
        compound = CompoundInterest(0, 10, 1)
        self.assertEqual(0, compound.get_interest())

    # Should return 100.00 given 100 principal, 0 percent, 10 years
    def test_given_100_0_10(self):
        compound = CompoundInterest(100, 0, 10)
        self.assertEqual(100, compound.get_interest())

    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month
    def test_add_1000_per_month(self):
        compound = CompoundInterest(100, 5, 8)
        self.assertEqual(118380.16, compound.with_contributions(1000))

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month
    
    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month


if __name__ == "__main__":
    unittest.main()
