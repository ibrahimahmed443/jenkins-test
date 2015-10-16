import unittest
from app import hello

class TestCases(unittest.TestCase):

	def test_hello(self):
		self.assertEqual(hello(), 'Hello Everyone!')

if __name__ == '__main__':
    unittest.main()
