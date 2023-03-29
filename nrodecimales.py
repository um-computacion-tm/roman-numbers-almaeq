def roman_to_decimal(roman_numeral):
    roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    decimal_num = 0
    for i in range(len(roman_numeral)):
        if i > 0 and roman_numerals[roman_numeral[i]] > roman_numerals[roman_numeral[i-1]]:
            decimal_num += roman_numerals[roman_numeral[i]] - 2 * roman_numerals[roman_numeral[i-1]]
        else:
            decimal_num += roman_numerals[roman_numeral[i]]
    return decimal_num
    
from parameterized import parameterized, parameterized_class
import unittest

class TestDecimalToRoman(unittest.TestCase):
    @parameterized.expand([
        ("I", 1),
        ("II", 2),
        ("III", 3),
        ("IV", 4),
        ("V", 5),
        ("VI", 6),
        ("VII", 7),
        ("VIII", 8),
        ("IX", 9),
        ("X", 10),
        ("XX", 20),
        ("XXXIV", 34),
        ("XL", 40),
        ("LIX", 59),
        ("XC", 90),
        ("CXXX", 130),
        ("CD", 400),
        ("D", 500),
        ("CMXCIX", 999),
        ("M", 1000),
        ("MMCCCXLIV", 2344)
    ])
    def test(self, roman, decimal):
        self.assertEqual(roman_to_decimal(roman),decimal)

if __name__ == '__main__':
    unittest.main()
