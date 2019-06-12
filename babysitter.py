class Babysitter:
	family_a_rates = ([23], [15, 20])

	def __init__(self, start_time, end_time, family):
		if start_time[-2:].upper() == "PM":
			self.start_time = int(start_time[:-5]) + 12
		else:
			self.start_time = int(start_time[:-5])

		if end_time[-2:].upper() == "PM":
			self.end_time = int(end_time[:-5]) + 12
		else:
			self.end_time = int(end_time[:-5])

		self.family = family.upper()

	def is_PM(self, time):
		if time <= 24 and time >= 17: return True
		return False

	def is_start_time_valid(self):
		return self.start_time >= 17 or self.start_time <= 4
		
	def is_end_time_valid(self):
		return self.end_time >= 17 or self.end_time <= 4

	def is_start_before_end(self):
		if self.end_time > self.start_time:
			return True
		if not self.is_PM(self.end_time) and self.is_PM(self.start_time):
			return True
		
		return False

	def is_family_valid(self):
		return self.family.upper() == "A" \
			or self.family.upper() == "B" \
			or self.family.upper() == "C"	

	def calculate_num_hrs(self, start, end):
		if end > start:
			return end - start
		if not self.is_PM(end) and self.is_PM(start):
			return (24 - start) + end
		return 0

	def calculate_family_a_rate(self):
		total = 0;

		for i in range(len(self.family_a_rates[0])):
			if i == 0:
				hours = self.calculate_num_hrs(self.start_time, self.family_a_rates[0][i])
				total += hours * self.family_a_rates[1][i]
		
		hours = self.calculate_num_hrs(self.family_a_rates[0][-1], self.end_time)
		total += hours * self.family_a_rates[1][-1]

		return total