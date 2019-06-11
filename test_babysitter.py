import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_starts_no_earlier_than_5pm(self):
		babysitter = Babysitter(5, 10, "a")
		self.assertEqual(babysitter.is_valid_start_time(), True)

		babysitter = Babysitter(4, 10, "a")
		self.assertEqual(babysitter.is_valid_start_time(), False)
