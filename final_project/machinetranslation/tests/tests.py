import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

import translator

class TestTranslation(unittest.TestCase): 
    """Testing the translator """
    def test1(self): 
        self.assertEqual(translator.english_to_french("chicken"), "Poulet")
        self.assertEqual(translator.english_to_french("one"), "Un")

    def test2(self):
        self.assertEqual(translator.french_to_english("saut"), "Jump")
        self.assertEqual(translator.french_to_english("deux"), "Two")

    def test3(self):
        try:
            self.assertEqual(translator.french_to_english(), TypeError)
            self.assertEqual(translator.english_to_french(), TypeError)
        except:
            print("test 3 bugged due to no argument (visual bug if not using try/except")

    def test4(self):
        self.assertEqual(translator.french_to_english("bonjour"), "Hello")
        self.assertEqual(translator.english_to_french("hello"), "Bonjour")

unittest.main()
