import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_starts_no_earlier_than_5pm(self):
		babysitter = Babysitter("5PM", "10PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

		babysitter = Babysitter("4PM", "10PM", "a")
		self.assertFalse(babysitter.is_start_time_valid())

		babysitter = Babysitter("1AM", "10PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

	def test_ends_no_later_than_4am(self):
		babysitter = Babysitter("6PM", "3AM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6PM", "10PM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6PM", "6AM", "a")
		self.assertFalse(babysitter.is_end_time_valid())

	def test_start_time_is_before_end_time(self):
		babysitter = Babysitter("6PM", "12PM", "a")
		self.assertTrue(babysitter.is_start_before_end())
		
		babysitter = Babysitter("1AM", "3AM", "a")
		self.assertTrue(babysitter.is_start_before_end())
		
		babysitter = Babysitter("6PM", "3AM", "a")
		self.assertTrue(babysitter.is_start_before_end())

		babysitter = Babysitter("8PM", "6PM", "a")
		self.assertFalse(babysitter.is_start_before_end())