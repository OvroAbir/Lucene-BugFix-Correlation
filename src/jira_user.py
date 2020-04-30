from .json_interface import Json_Jira_Issue_Interface

class User:
	def __init__(self, name, key, display_name, user_url):
		self.__name = name
		self.__key = key
		self.__display_name = display_name
		self.__user_url = user_url

	def __init__(self, user_json):
		(name, key, display_name, user_url) = User.get_user_from_json(user_json)
		self.__init__(name, key, display_name, user_url)

	def get_name(self):
		return self.__name

	def get_key(self):
		return self.__key

	def get_display_name(self):
		return self.__display_name

	def get_user_url(self):
		return self.__user_url

	@staticmethod
	def get_user_from_json(user_json):
		if (user_json == None):
			return None
		name = Json_Jira_Issue_Interface.__init_value("name", user_json)
		key = Json_Jira_Issue_Interface.__init_value("key", user_json)
		display_name = Json_Jira_Issue_Interface.__init_value("displayName", user_json)
		self_url = Json_Jira_Issue_Interface.__init_value("self", user_json)

		return User(name, key, display_name, self_url)
