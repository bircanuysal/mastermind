#!/usr/bin/env python3

from mastermind.utils.str_validator import StrValidator
import unittest


class StrValidator_Test(unittest.TestCase):
    """
    Tests for the StrValidator class.
    """

    def test_is_alpha_or_space_truthy(self):
        """
        Test is_alpha_or_space() for truthy returns.
        """
        sv = StrValidator()
        self.assertTrue(sv.is_alpha_or_space("Tu"))
        self.assertTrue(sv.is_alpha_or_space("Tu Vo"))

    def test_is_alpha_or_space_falsy(self):
        """
        Test is_alpha_or_space() for falsy returns.
        """
        sv = StrValidator()
        self.assertFalse(sv.is_alpha_or_space("2"))
        self.assertFalse(sv.is_alpha_or_space("Tu2"))
        self.assertFalse(sv.is_alpha_or_space("Tu!"))
        self.assertFalse(sv.is_alpha_or_space("   "))

    def test_capitalize(self):
        """
        Test capitalize() for correct return values.
        """
        sv = StrValidator()
        self.assertEqual(sv.capitalize("tu"), "Tu")
        self.assertEqual(sv.capitalize("tu vo"), "Tu Vo")
        self.assertEqual(sv.capitalize("tu  vo"), "Tu Vo")
        self.assertEqual(sv.capitalize("mr. tu vo"), "Mr. Tu Vo")


if __name__ == '__main__':
    unittest.main()
