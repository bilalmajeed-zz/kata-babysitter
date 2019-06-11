class Babysitter:
	def __init__(self, start_time, end_time, family):
		self.start_time = start_time
		self.end_time = end_time
		self.family = family

	def is_valid_start_time(self):
		if self.start_time < 5:
			return False
		return True