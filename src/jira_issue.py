from .jira_user import User
from .json_interface import Json_Jira_Issue_Interface
from .jira_issue_comment import Jira_Issue_Comment
from .jira_attachment import Jira_Attachment


class Jira_Issue:
	def __init__(self, json_data):
		self.__id = Json_Jira_Issue_Interface.init_value_from_json("id", json_data)
		self.__issue_rest_api_link = Json_Jira_Issue_Interface.init_value_from_json("self", json_data)
		self.__issue_key = Json_Jira_Issue_Interface.init_value_from_json("key", json_data)
		self.__priority = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "priority", "name")
		self.__assignee = Json_Jira_Issue_Interface.init_object_from_nested_json(json_data, User, "fields", "assignee")
		self.__issue_status = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "status", "name")
		self.__issue_creator = Json_Jira_Issue_Interface.init_object_from_nested_json(json_data, User, "fields", "creator")
		self.__issue_reporter = Json_Jira_Issue_Interface.init_object_from_nested_json(json_data, User, "fields", "reporter")
		self.__issue_type = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "issuetype", "name")
		self.__project_name = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "project", "name")
		self.__project_id = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "project", "id")
		self.__issue_creation_time = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "created")
		self.__issue_description = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "description")
		self.__time_spent = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "timetracking", "timeSpent")
		self.__issue_summary = Json_Jira_Issue_Interface.init_value_from_nested_json(json_data, "fields", "summary")
		self.__comments = Json_Jira_Issue_Interface.init_array_from_json(json_data, Jira_Issue_Comment, "fields", "comment",
																		 "comments")
		self.__attachments = Json_Jira_Issue_Interface.init_array_from_json(json_data, Jira_Attachment, "fields",
																			"attachment")

	def __str__(self):
		result ="Issue: (id: {}, link: {}, key: {}, priority: {}, assignee: {}, status: {}, creator: {}, reporter: {}, " \
				"type: {}, project name: {}, project_id: {}, issue created: {}, issue description: {}, time spent: {}, " \
				"issue summary: {}, comments: {}, attachments: {} )" \
			.format(self.__id, self.__issue_rest_api_link, self.__issue_key, self.__priority, self.__assignee,
					self.__issue_status, \
					self.__issue_creator, self.__issue_reporter, self.__issue_type,
					self.__project_name, \
					self.__project_id, self.__issue_creation_time, self.__issue_description, self.__time_spent,
					self.__issue_summary, \
					self.__comments, self.__attachments)
		return result

	def __repr__(self):
		return self.__str__()
