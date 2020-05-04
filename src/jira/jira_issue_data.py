from src.common.urllib_utils import UrlLibUtil
from src.jira.jira_issue_changelog import Jira_Issue_ChangeLog_History
from src.jira.jira_issue_remotelink import JiraIssueRemoteLink
from src.jira.jira_user import JiraUser
from src.common.json_interface import JsonJiraIssueInterface
from src.jira.jira_issue_comment import JiraIssueComment
from src.jira.jira_attachment import JiraAttachment


class JiraIssueData:
	def __init__(self, json_data):
		self.__id = JsonJiraIssueInterface.init_value_from_json("id", json_data)
		self.__issue_rest_api_link = JsonJiraIssueInterface.init_value_from_json("self", json_data)
		self.__issue_key = JsonJiraIssueInterface.init_value_from_json("key", json_data)
		self.__priority = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "priority", "name")
		self.__assignee = JsonJiraIssueInterface.init_object_from_nested_json(json_data, JiraUser, "fields", "assignee")
		self.__issue_status = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "status",
																					"name")
		self.__issue_creator = JsonJiraIssueInterface.init_object_from_nested_json(json_data, JiraUser, "fields",
																					  "creator")
		self.__issue_reporter = JsonJiraIssueInterface.init_object_from_nested_json(json_data, JiraUser, "fields",
																					   "reporter")
		self.__issue_type = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "issuetype",
																				  "name")
		self.__project_name = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "project",
																					"name")
		self.__project_id = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "project", "id")
		self.__issue_creation_time = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields",
																						   "created")
		self.__issue_description = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields",
																						 "description")
		self.__time_spent = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "timetracking",
																				  "timeSpent")
		self.__issue_summary = JsonJiraIssueInterface.init_value_from_nested_json(json_data, "fields", "summary")
		self.__comments = JsonJiraIssueInterface.init_array_from_json(json_data, JiraIssueComment, "fields",
																		 "comment",
																		 "comments")
		self.__attachments = JsonJiraIssueInterface.init_array_from_json(json_data, JiraAttachment, "fields",
																			"attachment")
		self.__changelog = JsonJiraIssueInterface.init_array_from_json(json_data, Jira_Issue_ChangeLog_History,
																		  "changelog",
																		  "histories")
		self.__remotelinks = JsonJiraIssueInterface.init_array_from_json(UrlLibUtil.download_and_parse_json(self.__issue_rest_api_link + "/remotelink"),
																		 JiraIssueRemoteLink)

	@property
	def changelog(self):
		return self.__changelog

	@property
	def created(self):
		return self.__issue_creation_time

	@property
	def attachments(self):
		return self.__attachments

	@property
	def comments(self):
		return self.__comments

	@property
	def creator(self):
		return self.__issue_creator

	@property
	def reporter(self):
		return self.__issue_reporter

	@property
	def assignee(self):
		return self.__assignee

	@property
	def issue_key(self):
		return self.__issue_key

	@property
	def remote_links(self):
		return self.__remotelinks

	@property
	def rest_link(self):
		return self.__issue_rest_api_link

	def __str__(self):
		result = "Issue: (id: {}, link: {}, key: {}, priority: {}, assignee: {}, status: {}, creator: {}, reporter: {}, " \
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
