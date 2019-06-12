import unittest
from babysitter import Babysitter

class TestBabysitter(unittest.TestCase):
	def test_that_the_start_time_no_earlier_than_5pm(self):
		babysitter = Babysitter("5:00PM", "10:00PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

		babysitter = Babysitter("4:00PM", "10:00PM", "a")
		self.assertFalse(babysitter.is_start_time_valid())

		babysitter = Babysitter("1:00AM", "10:00PM", "a")
		self.assertTrue(babysitter.is_start_time_valid())

		babysitter = Babysitter("4:45PM", "10:00PM", "a")
		self.assertFalse(babysitter.is_start_time_valid())

	def test_that_the_end_time_no_later_than_4am(self):
		babysitter = Babysitter("6:00PM", "3:00AM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6:00PM", "10:00PM", "a")
		self.assertTrue(babysitter.is_end_time_valid())

		babysitter = Babysitter("6:00PM", "6:00AM", "a")
		self.assertFalse(babysitter.is_end_time_valid())

		babysitter = Babysitter("6:00PM", "4:30AM", "a")
		self.assertFalse(babysitter.is_end_time_valid())

	def test_that_the_start_time_is_before_end_time(self):
		babysitter = Babysitter("6:00PM", "12:00PM", "a")
		self.assertTrue(babysitter.is_start_before_end(18, 24))
		
		babysitter = Babysitter("1:00AM", "3:00AM", "a")
		self.assertTrue(babysitter.is_start_before_end(1, 3))
		
		babysitter = Babysitter("6:00PM", "3:00AM", "a")
		self.assertTrue(babysitter.is_start_before_end(18, 3))

		babysitter = Babysitter("8:00PM", "6:00PM", "a")
		self.assertFalse(babysitter.is_start_before_end(20, 18))

		babysitter = Babysitter("1:00AM", "11:00PM", "a")
		self.assertFalse(babysitter.is_start_before_end(1, 23))

	def test_that_a_selected_family_name_is_valid_or_not(self):
		babysitter = Babysitter("8:00PM", "6:00PM", "a")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "b")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "c")
		self.assertTrue(babysitter.is_family_valid())

		babysitter = Babysitter("8:00PM", "6:00PM", "d")
		self.assertFalse(babysitter.is_family_valid())

	def test_that_the_correct_number_of_hrs_between_start_and_end_time_is_calculated(self):
		babysitter = Babysitter("7:00PM", "2:00AM", "a")
		self.assertEqual(babysitter.calculate_num_hrs(19, 2), 7)

		babysitter = Babysitter("7:00PM", "12:00PM", "a")
		self.assertEqual(babysitter.calculate_num_hrs(19, 24), 5)

	def test_that_the_correct_rate_is_calculated_when_family_A_is_selected(self):
		babysitter = Babysitter("7:00PM", "11:00PM", "a")
		self.assertEqual(babysitter.calculate_rate(), 60)

		babysitter = Babysitter("7:00PM", "2:00AM", "a")
		self.assertEqual(babysitter.calculate_rate(), 120)

		babysitter = Babysitter("7:00PM", "10:00PM", "a")
		self.assertEqual(babysitter.calculate_rate(), 45)

	def test_that_the_correct_rate_is_calculated_when_family_B_is_selected(self):
		babysitter = Babysitter("7:00PM", "9:00PM", "b")
		self.assertEqual(babysitter.calculate_rate(), 24)

		babysitter = Babysitter("7:00PM", "11:00PM", "b")
		self.assertEqual(babysitter.calculate_rate(), 44)

		babysitter = Babysitter("7:00PM", "2:00AM", "b")
		self.assertEqual(babysitter.calculate_rate(), 84)

	def test_that_the_correct_rate_is_calculated_when_family_C_is_selected(self):
		babysitter = Babysitter("6:00PM", "8:00PM", "c")
		self.assertEqual(babysitter.calculate_rate(), 42)

		babysitter = Babysitter("6:00PM", "11:00PM", "c")
		self.assertEqual(babysitter.calculate_rate(), 93)

		babysitter = Babysitter("6:00PM", "2:00AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 138)

	def test_that_only_full_hour_rates_are_calculated(self):
		babysitter = Babysitter("6:30PM", "2:45AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 138)

		babysitter = Babysitter("6:30PM", "2:30AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 138)

		babysitter = Babysitter("6:30PM", "1:45AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 123)

	def test_that_rates_are_only_calaculated_if_inputs_are_valid(self):
		babysitter = Babysitter("6:30PM", "1:45AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 123)

		babysitter = Babysitter("4:30PM", "1:45AM", "c")
		self.assertEqual(babysitter.calculate_rate(), 0)

		babysitter = Babysitter("6:30PM", "4:55AM", "a")
		self.assertEqual(babysitter.calculate_rate(), 0)

		babysitter = Babysitter("6:30PM", "1:45AM", "s")
		self.assertEqual(babysitter.calculate_rate(), 0)

		babysitter = Babysitter("1:00AM", "11:00PM", "a")
		self.assertEqual(babysitter.calculate_rate(), 0)