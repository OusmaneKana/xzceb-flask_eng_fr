import unittest
from translator import WatsonTranslator


agent = WatsonTranslator()
class TestingENToFR(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.english_to_french("Hello"),"Bonjour")
		self.assertNotEqual(agent.english_to_french("Hello"),"Dormir")
		
class TestingFRToEN(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.french_to_english("Bonjour"),"Hello")
		self.assertNotEqual(agent.french_to_english("Bonjour"),"Good Bye")




if __name__ == '__main__':
	unittest.main()