"""
	Work in progress
"""
class Clock():
	"""
		Represents global clock
	"""
	def __init__(self):
		""" Set current time default """
		self.current_time = 0

	def get_current_time(self):
		""" Returns current time """
		return self.current_time