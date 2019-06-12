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

	def test_family_name_is_valid(self):
		babysitter = Babysitter("8:00PM", "6:00PM", "a")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "b")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "c")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "d")
		self.assertFalse(babysitter.is_family_valid())

	def test_if_the_number_of_hrs_between_start_and_end_time_is_correct(self):
		babysitter = Babysitter("7:00PM", "2:00AM", "a")
		self.assertEqual(babysitter.calculate_num_hrs(19, 2), 7)

		babysitter = Babysitter("7:00PM", "12:00PM", "a")
		self.assertEqual(babysitter.calculate_num_hrs(19, 24), 5)

	def test_that_the_correct_rate_is_calculated_when_family_A_is_selected(self):
		babysitter = Babysitter("7:00PM", "11:00PM", "a")
		self.assertEqual(babysitter.calculate_family_a_rate(), 60)

		babysitter = Babysitter("7:00PM", "2:00AM", "a")
		self.assertEqual(babysitter.calculate_family_a_rate(), 120)