class Babysitter:
	def __init__(self, start_time, end_time, family):
		self.start_time = start_time
		self.end_time = end_time
		self.family = family

	def check_valid_time(self, time, am_pm):
		if am_pm == "PM":
			if time >= 5 and time <= 12:
				return True
		elif am_pm == "AM":
			if time >= 1 and time <= 4:
				return True

		return False

	def is_start_time_valid(self):
		am_pm = self.start_time[-2:].upper()
		time = int(self.start_time[:-2])
		return self.check_valid_time(time, am_pm)
		

	def is_end_time_valid(self):
		am_pm = self.end_time[-2:].upper()
		time = int(self.end_time[:-2])
		return self.check_valid_time(time, am_pm)