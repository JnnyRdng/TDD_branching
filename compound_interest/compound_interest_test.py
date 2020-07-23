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
        self.assertEqual(10, compound.percent)

    def test_has_years_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(20, compound.years)

    def test_has_frequency_property(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(12, compound.frequency)

    # Should return 732.81 given 100 principal, 10 percent, 20 years
    def test_call_get_interest_function(self):
        compound = CompoundInterest(100, 10, 20)
        self.assertEqual(None, compound.get_interest())

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month


if __name__ == "__main__":
    unittest.main()
