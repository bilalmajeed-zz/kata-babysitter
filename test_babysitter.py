import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_starts_no_earlier_than_5pm(self):
		babysitter = Babysitter("5PM", "10PM", "a")
		self.assertEqual(babysitter.is_start_time_valid(), True)

		babysitter = Babysitter("4PM", "10PM", "a")
		self.assertEqual(babysitter.is_start_time_valid(), False)

		babysitter = Babysitter("1AM", "10PM", "a")
		self.assertEqual(babysitter.is_start_time_valid(), True)

	def test_ends_no_later_than_4am(self):
		babysitter = Babysitter("6PM", "3AM", "a")
		self.assertEqual(babysitter.is_end_time_valid(), True)

		babysitter = Babysitter("6PM", "10PM", "a")
		self.assertEqual(babysitter.is_end_time_valid(), True)

		babysitter = Babysitter("6PM", "6AM", "a")
		self.assertEqual(babysitter.is_end_time_valid(), False)