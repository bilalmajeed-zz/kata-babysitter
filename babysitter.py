class Babysitter:
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

	def is_start_time_valid(self):
		return self.start_time >= 17 or self.start_time <= 4
		
	def is_end_time_valid(self):
		return self.end_time >= 17 or self.end_time <= 4

	def is_start_before_end(self):
		if self.end_time > self.start_time:
			return True
		else:
			if self.end_time >= 1 and self.end_time <= 4 \
			and self.start_time > 17 and self.end_time < 24:
				return True
		return False

	def is_family_valid(self):
		return self.family.upper() == "A" \
			or self.family.upper() == "B" \
			or self.family.upper() == "C"