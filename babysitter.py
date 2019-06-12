class Babysitter:
	family_rates = {'A': ([23], [15, 20]), 
					'B': ([22, 24], [12, 8, 16]),
					'C': ([21], [21, 15])}

	def __init__(self, start_time, end_time, family):
		""" Init function, set up all the object data memebers """

		if start_time[-2:].upper() == "PM":
			self.start_time = int(start_time[:-5]) + 12
		else:
			self.start_time = int(start_time[:-5])

		if end_time[-2:].upper() == "PM":
			self.end_time = int(end_time[:-5]) + 12
		else:
			self.end_time = int(end_time[:-5])

		if end_time[-4:-2] != "00":
			self.end_time_has_minutes = True
		else:
			self.end_time_has_minutes = False

		self.family = family.upper()

	def is_PM(self, time):
		""" Return True if the given time is in the PM, else return False """
		if time <= 24 and time >= 17: return True
		return False

	def is_start_time_valid(self):
		""" Verify if the start time of the object is valid """
		return self.start_time >= 17 or self.start_time <= 4
		
	def is_end_time_valid(self):
		""" Verify if the the end time of object is valid """
		if self.end_time == 4 and self.end_time_has_minutes:
			return False
		return self.end_time >= 17 or self.end_time <= 4

	def is_start_before_end(self, start, end):
		""" Check if the start time is before the ene time, given in the params """
		if not self.is_PM(end) and self.is_PM(start):
			return True
		elif not self.is_PM(start) and self.is_PM(end):
			return False

		if end > start:
			return True
		
		return False

	def is_family_valid(self):
		""" Verify that the entered family name is valid """
		return self.family == "A" \
			or self.family == "B" \
			or self.family == "C"	

	def calculate_num_hrs(self, start, end):
		""" Calculate the number of between the start and end params"""
		if end > start:
			return end - start
		if not self.is_PM(end) and self.is_PM(start):
			return (24 - start) + end
		return 0

	def is_valid_input(self):
		""" Test all inputs to class to make sure they are valid """
		return self.is_start_time_valid() and \
			   self.is_end_time_valid() and \
			   self.is_start_before_end(self.start_time, self.end_time) and \
			   self.is_family_valid()

	def calculate_rate(self):
		if not self.is_valid_input(): 
			return 0

		total = 0;
		done = 0
		rates = self.family_rates[self.family]

		for i in range(len(rates[0])):
			if i == 0:
				if self.is_start_before_end(rates[0][i], self.end_time):
					hours = self.calculate_num_hrs(self.start_time, rates[0][i])
				else: 
					hours = self.calculate_num_hrs(self.start_time, self.end_time)
					done = 1
				total += hours * rates[1][i]
			else: 
				if self.is_start_before_end(rates[0][i], self.end_time):
					hours = self.calculate_num_hrs(rates[0][i-1], rates[0][i])
				else: 
					hours = self.calculate_num_hrs(rates[0][i-1], self.end_time)
					done = 1
				total += hours * rates[1][i]

			if done == 1:
				break
		
		hours = self.calculate_num_hrs(rates[0][-1], self.end_time)
		total += hours * rates[1][-1]

		return total

if __name__ == '__main__':
	import argparse

	parser = argparse.ArgumentParser(description='Calculate the pay rate of a babysitter \
									based on their start and end times and the specific \
									family to babysit')
	parser.add_argument("start_time", type=str)
	parser.add_argument("end_time", type=str)
	parser.add_argument("family", type=str)
	args = parser.parse_args()

	babysitter = Babysitter(args.start_time, args.end_time, args.family)
	pay = babysitter.calculate_rate()

	if pay == 0:
		print("""
		The given inputs were invalid
		
		Expected format: 
		python babysitter.py START_TIME END_TIME FAMILY

		START_TIME \t Should be between '5:00PM' and '4:00AM'
		END_TIME \t Should be between '5:00PM' and '4:00AM'
		FAMILY \t\t Should be either 'A', 'B', or 'C'
		""")
	else:
		print("To babysit for family {} if you start at {} and end at {}, you should get paid ${}" \
			.format(args.family.upper(), args.start_time, args.end_time, pay))