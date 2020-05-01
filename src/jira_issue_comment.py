from .jira_user import User
from .json_interface import Json_Jira_Issue_Interface

class Jira_Issue_Comment:
	def __init__(self, comment_rest_url, comment_id, author_name, author_key, author_display_name, author_url,
				 comment_body, comment_creation_time):
		self.__comment_creation_time = comment_creation_time
		self.__comment_body = comment_body
		self.__author = User(author_name, author_key, author_display_name, author_url)
		self.__comment_id = comment_id
		self.__comment_rest_url = comment_rest_url

	@classmethod
	def get_object_from_json(cls, json_comment_data):
		comment_rest_url = Json_Jira_Issue_Interface.init_value_from_json("self", json_comment_data)
		comment_id = Json_Jira_Issue_Interface.init_value_from_json("id", json_comment_data)
		author_name = Json_Jira_Issue_Interface.init_value_from_nested_json(json_comment_data, "author", "name")
		author_key = Json_Jira_Issue_Interface.init_value_from_nested_json(json_comment_data, "author", "key")
		author_display_name = Json_Jira_Issue_Interface.init_value_from_nested_json(json_comment_data, "author", "displayName")
		author_rest_url = Json_Jira_Issue_Interface.init_value_from_nested_json(json_comment_data, "author", "self")
		comment_body = Json_Jira_Issue_Interface.init_value_from_json("body", json_comment_data)
		comment_creation_time = Json_Jira_Issue_Interface.init_value_from_json("created", json_comment_data)

		return cls(comment_rest_url, comment_id, author_name, author_key, author_display_name, author_rest_url, comment_body, comment_creation_time)

	def __str__(self):
		return "Comment:(url: {}, id: {}, author: {}, body: {}, created: {})"\
			.format(self.__comment_rest_url, self.__comment_id, self.__author, self.__comment_body, self.__comment_creation_time)

	def __repr__(self):
		return self.__str__()
