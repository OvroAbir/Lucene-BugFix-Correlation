from src.common.json_interface import Json_Jira_Issue_Interface


class User:
	def __init__(self, name, key, display_name, user_url):
		self.__name = name
		self.__key = key
		self.__display_name = display_name
		self.__user_url = user_url

	@property
	def name(self):
		return self.__name

	@property
	def key(self):
		return self.__key

	@property
	def display_name(self):
		return self.__display_name

	@property
	def user_url(self):
		return self.__user_url

	def __str__(self):
		return "User: ( name: {}, key: {}, display name: {}, url: {} )\n" \
			.format(self.__name, self.__key, self.__display_name, self.__user_url)

	def __repr__(self):
		return self.__str__()

	@classmethod
	def get_object_from_json(cls, json_obj):
		if json_obj is None:
			return None
		name = Json_Jira_Issue_Interface.init_value_from_json("name", json_obj)
		key = Json_Jira_Issue_Interface.init_value_from_json("key", json_obj)
		display_name = Json_Jira_Issue_Interface.init_value_from_json("displayName", json_obj)
		self_url = Json_Jira_Issue_Interface.init_value_from_json("self", json_obj)

		return cls(name, key, display_name, self_url)
