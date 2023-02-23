import unittest
from translator import WatsonTranslator


agent = WatsonTranslator()
class TestingENToFR(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.englishToFrench("Hello"),"Bonjour")



class TestingFRToEN(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.frenchToEnglish("Bonjour"),"Hello")



if __name__ == '__main__':
	unittest.main()