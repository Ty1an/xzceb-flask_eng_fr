import unittest
from machinetranslation import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):

    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello")._to_dict()["result"]["translations"][0]["translation"], "Bonjour")
        self.assertEqual(english_to_french(None), "")


    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour")._to_dict()["result"]["translations"][0]["translation"], "Hello")
        self.assertEqual(french_to_english(None), "")


if __name__ == '__main__':
    unittest.main()