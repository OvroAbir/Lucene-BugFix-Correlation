from .jira_issue_data import Jira_Issue_Data

class Jira_Issue:
	def __init__(self, json_data):
		self.__data = Jira_Issue_Data(json_data)
		self.__fix_time = 0