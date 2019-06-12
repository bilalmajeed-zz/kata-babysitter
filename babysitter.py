class Babysitter:
	family_rates = {'A': ([23], [15, 20]), 
					'B': ([22, 24], [12, 8, 16]),
					'C': ([21], [21, 15])}

	def __init__(self, start_time, end_time, family):
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
		if time <= 24 and time >= 17: return True
		return False

	def is_start_time_valid(self):
		return self.start_time >= 17 or self.start_time <= 4
		
	def is_end_time_valid(self):
		if self.end_time == 4 and self.end_time_has_minutes:
			return False
		return self.end_time >= 17 or self.end_time <= 4

	def is_start_before_end(self, start, end):
		if end > start:
			return True
		if not self.is_PM(end) and self.is_PM(start):
			return True
		
		return False

	def is_family_valid(self):
		return self.family == "A" \
			or self.family == "B" \
			or self.family == "C"	

	def calculate_num_hrs(self, start, end):
		if end > start:
			return end - start
		if not self.is_PM(end) and self.is_PM(start):
			return (24 - start) + end
		return 0

	def calculate_rate(self):
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