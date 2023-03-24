def decimal_to_roman(decimal):
    total = ''
    
    if decimal == 1000:
        total += 'M'
    if 400 > decimal >= 100:
        centena = decimal // 100
        total += 'C' * centena
        decimal = decimal % 100 
    if 500 > decimal >= 400:
        total += "CD"
        decimal = decimal % 100
    if 900 > decimal >= 500:
        total += 'D'
        decimal -= 500
        centena = decimal //100
        total += 'C' * centena
        decimal = decimal % 100
    if 1000 > decimal >= 900:
        total += "CM"
        decimal = decimal % 100
    if 40 > decimal >= 10:
        decena = decimal // 10
        total += "X" * decena
        decimal = decimal % 10
    if 50 > decimal >= 40:
        total += "XL"
        decimal = decimal % 10
    if 90 > decimal >= 50:
        total += 'L' 
        decimal -= 50
        decena = decimal // 10
        total += "X" * decena
        decimal = decimal % 10
    if 100 > decimal >= 90:
        total += "XC"
        decimal = decimal % 10
    if decimal <= 3:
        total += 'I' * decimal
    if decimal == 4:
        total += "IV"
    elif 9 > decimal >= 5:
        total += 'V'
        decimal -= 5
        unidad = decimal % 10
        total += "I" * unidad
    elif decimal == 9:
        total += "IX"
    return total

from parameterized import parameterized, parameterized_class
import unittest

class TestDecimalToRoman(unittest.TestCase):
    @parameterized.expand([
        (1, "I"),
        (2, "II"),
        (3, "III"),
        (4, "IV"),
        (5, "V"),
        (6, "VI"),
        (7, "VII"),
        (8, "VIII"),
        (9, "IX"),
        (10, "X"),
        (11, "XI"),
        (12, "XII"),
        (13, "XIII"),
        (14, "XIV"),
        (15, "XV"),
        (16, "XVI"),
        (17, "XVII"),
        (18, "XVIII"),
        (19, "XIX"),
        (20, "XX"),
        (33, "XXXIII"),
        (35, "XXXV"),
        (36, "XXXVI"),
        (37, "XXXVII"),
        (38, "XXXVIII"),
        (39, "XXXIX"),
        (40, "XL"),
        (44, "XLIV"),
        (49, "XLIX"),
        (50, "L"), 
        (52, "LII"),
        (54, "LIV"),
        (57, "LVII"),
        (59, "LIX"),
        (60, "LX"),
        (64, "LXIV"),
        (65, "LXV"),
        (68, "LXVIII"),
        (69, "LXIX"),
        (70, "LXX"),
        (71, "LXXI"),
        (84, "LXXXIV"),
        (89, "LXXXIX"),
        (90, "XC"),
        (91, "XCI"),
        (94, "XCIV"),
        (98, "XCVIII"),
        (99, "XCIX"),
        (100, "C"),
        (398, "CCCXCVIII"),
        (399, "CCCXCIX"),
        (400, "CD"),
        (498, "CDXCVIII"),
        (499, "CDXCIX"),
        (500, "D"),
        (890, "DCCCXC"),
        (898, "DCCCXCVIII"),
        (899, "DCCCXCIX"),
        (900, "CM"),
        (940, "CMXL"),
        (950, "CML"),
        (980, "CMLXXX"), 
        (998, "CMXCVIII"), 
        (999, "CMXCIX"),
        (1000, "M")
    ])
    def test(self, decimal, roman):
        self.assertEqual(decimal_to_roman(decimal), roman)

"""class TestDecimalToRoman(unittest.TestCase):
    def test_uno(self):
        #pre condicion
        #NO HAY 
        #proceso 
        resultado = decimal_to_roman(1)
        self.assertEqual(resultado, "I")
"""
if __name__ == '__main__':
    unittest.main()
