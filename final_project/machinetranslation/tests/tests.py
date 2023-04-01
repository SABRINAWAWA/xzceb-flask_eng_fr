import unittest
from machinetranslation.translator import french_to_english, english_to_french

class Testing(unittest.TestCase):
    def test_null_input_frechToEnglish(self):
        self.assertNotEqual(french_to_english("NULL"), "Hello")

    def test_output_frechToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")

    def test_null_input_englishToFrench(self):
        self.assertNotEqual(english_to_french("NULL"), "Bonjour")

    def test_output_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")

if __name__ == '__main__':
    unittest.main()