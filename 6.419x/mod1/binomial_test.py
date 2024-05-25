import unittest
from binomial import calculate_binomial_probability

class TestBinomial(unittest.TestCase):
    def test_case_1(self):
        self.assertAlmostEqual(calculate_binomial_probability(10, 5, 0.5), 0.24609375)

    def test_case_2(self):
        self.assertAlmostEqual(calculate_binomial_probability(100, 20, 0.2), 0.11422705610254359)

    def test_case_3(self):
        self.assertAlmostEqual(calculate_binomial_probability(1000, 100, 0.01), 0.03867663558244387)

    def test_case_4(self):
        self.assertAlmostEqual(calculate_binomial_probability(50, 0, 0.5), 0.000888178419700748)

    def test_case_5(self):
        self.assertAlmostEqual(calculate_binomial_probability(100, 100, 0.5), 7.888609052210118e-31)

if __name__ == '__main__':
    unittest.main()