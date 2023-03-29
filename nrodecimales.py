def roman_to_decimal(roman):
    decimal = 0

    for letra in roman:
        if letra == 'I':
            decimal += 1
        elif letra == 'V':
            if decimal > 0:
                decimal -= 1
            decimal += 5
        elif letra == "X":
            if decimal > 0:
                decimal = -1
            decimal += 10

    return decimal

from parameterized import parameterized, parameterized_class
import unittest

class TestDecimalToRoman(unittest.TestCase):
    @parameterized.expand([
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("V", 5),
        ("X", 10)
    ])
    def test(self, roman, decimal):
        self.assertEqual(roman_to_decimal(roman),decimal)

if __name__ == '__main__':
    unittest.main()
