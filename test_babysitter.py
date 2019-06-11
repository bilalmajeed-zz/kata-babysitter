import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_starts_no_earlier_than_5pm(self):
		babysitter = Babysitter("5PM", "10PM", "a")
		self.assertEqual(babysitter.is_valid_start_time(), True)

		babysitter = Babysitter("4PM", "10PM", "a")
		self.assertEqual(babysitter.is_valid_start_time(), False)

		babysitter = Babysitter("1AM", "10PM", "a")
		self.assertEqual(babysitter.is_valid_start_time(), True)
