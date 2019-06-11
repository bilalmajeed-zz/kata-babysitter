import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_starts_no_earlier_than_5pm(self):
		babysitter = Babysitter("5:00PM", "10:00PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

		babysitter = Babysitter("4:00PM", "10:00PM", "a")
		self.assertFalse(babysitter.is_start_time_valid())

		babysitter = Babysitter("1:00AM", "10:00PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

	def test_ends_no_later_than_4am(self):
		babysitter = Babysitter("6:00PM", "3:00AM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6:00PM", "10:00PM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6:00PM", "6:00AM", "a")
		self.assertFalse(babysitter.is_end_time_valid())

	def test_start_time_is_before_end_time(self):
		babysitter = Babysitter("6:00PM", "12:00PM", "a")
		self.assertTrue(babysitter.is_start_before_end())
		
		babysitter = Babysitter("1:00AM", "3:00AM", "a")
		self.assertTrue(babysitter.is_start_before_end())
		
		babysitter = Babysitter("6:00PM", "3:00AM", "a")
		self.assertTrue(babysitter.is_start_before_end())

		babysitter = Babysitter("8:00PM", "6:00PM", "a")
		self.assertFalse(babysitter.is_start_before_end())