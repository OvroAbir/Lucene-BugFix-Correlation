from dateutil import parser as timeparser


class TimeUtil:
	@staticmethod
	def get_time_diff(time_str1:str, time_str2:str):
		time1 = timeparser.parse(time_str1)
		time2 = timeparser.parse(time_str2)
		return abs((time2-time1).total_seconds())

	@staticmethod
	def convert_seconds_to_hours(time_seconds):
		hours = []
		for sec in time_seconds:
			hours.append(sec/3600.0)
		return hours

	@staticmethod
	def convert_seconds_to_days(time_seconds):
		days = []
		for sec in time_seconds:
			days.append(sec / 3600.0 / 24.0)
		return days

