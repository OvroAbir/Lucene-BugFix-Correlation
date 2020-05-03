from dateutil import parser as timeparser


class TimeUtil:
	@staticmethod
	def get_time_diff(time_str1:str, time_str2:str):
		time1 = timeparser(time_str1)
		time2 = timeparser(time_str2)
		return abs(time2.total_seconds() - time1.total_seconds())