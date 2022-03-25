
import unittest

from num_converters import num_to_roman, roman_to_num


class TestConvertersNumToRoman(unittest.TestCase):

    def test_num_to_roman_5(self):
        self.assertEqual(num_to_roman(5), 'V')

    def test_num_to_roman_15(self):
        self.assertEqual(num_to_roman(15), 'XV')

    def test_num_to_roman_20(self):
        self.assertEqual(num_to_roman(20), 'XX')

    def test_num_to_roman_30(self):
        self.assertEqual(num_to_roman(30), 'XXX')

    def test_num_to_roman_40(self):
        self.assertEqual(num_to_roman(40), 'XL')

    def test_num_to_roman_50(self):
        self.assertEqual(num_to_roman(50), 'L')

    def test_num_to_roman_55(self):
        self.assertEqual(num_to_roman(55), 'LV')

    def test_num_to_roman_60(self):
        self.assertEqual(num_to_roman(60), 'LX')

    def test_num_to_roman_70(self):
        self.assertEqual(num_to_roman(70), 'LXX')

    def test_num_to_roman_80(self):
        self.assertEqual(num_to_roman(80), 'LXXX')

    def test_num_to_roman_90(self):
        self.assertEqual(num_to_roman(90), 'XC')

    def test_num_to_roman_100(self):
        self.assertEqual(num_to_roman(100), 'C')

    def test_num_to_roman_500(self):
        self.assertEqual(num_to_roman(500), 'D')

    def test_num_to_roman_538(self):
        self.assertEqual(num_to_roman(538), 'DXXXVIII')

    def test_num_to_roman_807(self):
        self.assertEqual(num_to_roman(807), 'DCCCVII')

    def test_num_to_roman_999(self):
        self.assertEqual(num_to_roman(999), 'CMXCIX')


class TestConvertersRomanToNum(unittest.TestCase):

    def test_roman_to_num_5(self):
        self.assertEqual(roman_to_num('V'), 5)

    def test_roman_to_num_15(self):
        self.assertEqual(roman_to_num('XV'), 15)

    def test_roman_to_num_20(self):
        self.assertEqual(roman_to_num('XX'), 20)

    def test_roman_to_num_500(self):
        self.assertEqual(roman_to_num('D'), 500)

    def test_roman_to_num_807(self):
        self.assertEqual(roman_to_num('DCCCVII'), 807)

    def test_roman_to_num_999(self):
        self.assertEqual(roman_to_num('CMXCIX'), 999)
