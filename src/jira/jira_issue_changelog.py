from src.jira.jira_user import User
from src.common.json_interface import Json_Jira_Issue_Interface


class Jira_Issue_ChangeLog_Item:
	def __init__(self, field, field_type, from_str, to_str):
		self.__field = field
		self.__field_type = field_type
		self.__from_str = from_str
		self.__to_str = to_str

	@property
	def field(self):
		return self.__field

	@property
	def field_type(self):
		return self.__field_type

	@property
	def from_str(self):
		return self.__from_str

	@property
	def to_str(self):
		return self.__to_str

	@classmethod
	def get_object_from_json(cls, json_obj):
		field = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "field")
		field_type = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "fieldtype")
		fromStr = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "fromString")
		toStr = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "toString")

		return cls(field, field_type, fromStr, toStr)


class Jira_Issue_ChangeLog_History:
	def __init__(self, id, created_time, author, items):
		self.__id = id
		self.__created_time = created_time
		self.__author = author
		self.__items = items

	@property
	def id(self):
		return self.__id

	@property
	def created_time(self):
		return self.__created_time

	@property
	def author(self):
		return self.__author

	@property
	def items(self):
		return self.__items

	@classmethod
	def get_object_from_json(cls, json_obj):
		id = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "id")
		author = Json_Jira_Issue_Interface.init_object_from_nested_json(json_obj, User, "author")
		created_time = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "created")
		items = Json_Jira_Issue_Interface.init_array_from_json(json_obj, Jira_Issue_ChangeLog_Item, "items")

		return cls(id, created_time, author, items)
