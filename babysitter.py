class Babysitter:
	def __init__(self, start_time, end_time, family):
		self.start_time = start_time
		self.end_time = end_time
		self.family = family

	def is_valid_start_time(self):
		am_pm = self.start_time[-2:].upper()
		time = int(self.start_time[:-2])

		if am_pm == "PM":
			if time >= 5 and time <= 12:
				return True
		elif am_pm == "AM":
			if time >= 1 and time <= 4:
				return True

		return False