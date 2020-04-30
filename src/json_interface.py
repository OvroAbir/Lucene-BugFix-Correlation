import json
from jira_user import User

class Json_Jira_Issue_Interface:

	@staticmethod
	def __init_value(key, json_obj):
		if(key in json_obj):
			return json_obj[key]
		return ""