import unittest
from translator import WatsonTranslator


agent = WatsonTranslator()
class TestingENToFR(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.englishToFrench("Hello"),"Bonjour")
		self.assertNotEqual(agent.englishToFrench("Hello"),"Dormir")
		
class TestingFRToEN(unittest.TestCase):
	def test1(self):
		self.assertEqual(agent.frenchToEnglish("Bonjour"),"Hello")
		self.assertNotEqual(agent.frenchToEnglish("Bonjour"),"Good Bye")




if __name__ == '__main__':
	unittest.main()