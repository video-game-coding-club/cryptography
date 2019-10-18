import unittest
from scripts.caesar import shift_character


class TestCaesarCipher(unittest.TestCase):

    def test_shift_character(self):
        self.assertEqual(shift_character("a", 1), "B")
        self.assertEqual(shift_character("a", 2), "C")
        self.assertEqual(shift_character("a", 3), "D")
        self.assertEqual(shift_character("z", 1), "A")
        self.assertEqual(shift_character("Z", 2), "B")
        self.assertEqual(shift_character("1", 2), "1")
        self.assertEqual(shift_character(",", 2), ",")
        self.assertEqual(shift_character(".", 2), ".")
        self.assertEqual(shift_character(";", 2), ";")
        self.assertEqual(shift_character(":", 2), ":")
        self.assertEqual(shift_character("!", 2), "!")
        self.assertEqual(shift_character("(", 2), "(")
        self.assertEqual(shift_character(")", 2), ")")
        self.assertEqual(shift_character("'", 2), "'")
        self.assertEqual(shift_character('"', 2), '"')
        self.assertEqual(shift_character("?", 2), "?")
        self.assertEqual(shift_character("-", 2), "-")
        with self.assertRaisesRegexp(Exception, "Illegal input"):
            shift_character("$", 1)
        with self.assertRaisesRegexp(Exception, "too long"):
            shift_character("ab", 1)
