import unittest
from translator import frenchToEnglish, englishToFrench

class TestFrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(frenchToEnglish(None), None)
    def test2(self):
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello')

class TestEnglish(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench(None), None)
    def test2(self):
        self.assertEqual(englishToFrench('Hello'), 'Bonjour')
    