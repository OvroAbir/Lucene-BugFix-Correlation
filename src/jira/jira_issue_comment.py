from src.jira.jira_user import JiraUser
from src.common.json_interface import JsonJiraIssueInterface
import re


class JiraIssueComment:
	def __init__(self, comment_rest_url, comment_id, author_name, author_key, author_display_name, author_url,
				 comment_body, comment_creation_time):
		self.__comment_creation_time = comment_creation_time
		self.__comment_body = comment_body
		self.__author = JiraUser(author_name, author_key, author_display_name, author_url)
		self.__comment_id = comment_id
		self.__comment_rest_url = comment_rest_url

	def __get_matched_str(self, pattern_str):
		pattern = re.compile(pattern_str)
		match = re.search(pattern, self.__comment_body)
		if match is None:
			return None
		return match.group()

	def get_commit_hash(self):
		hexaPattern = r'Commit\s([0-9a-fA-F]+)\s'
		res = self.__get_matched_str(hexaPattern)
		if res is None:
			return None
		return res[7:-1]

	def get_git_url(self):
		urlPattern = r'((git|ssh|http(s)?)|(git@[\w\.]+))(:(//)?).*(\.git)(/)?;h=([0-9a-fA-F])+'
		return self.__get_matched_str(urlPattern)

	@classmethod
	def get_object_from_json(cls, json_comment_data):
		comment_rest_url = JsonJiraIssueInterface.init_value_from_json("self", json_comment_data)
		comment_id = JsonJiraIssueInterface.init_value_from_json("id", json_comment_data)
		author_name = JsonJiraIssueInterface.init_value_from_nested_json(json_comment_data, "author", "name")
		author_key = JsonJiraIssueInterface.init_value_from_nested_json(json_comment_data, "author", "key")
		author_display_name = JsonJiraIssueInterface.init_value_from_nested_json(json_comment_data, "author", "displayName")
		author_rest_url = JsonJiraIssueInterface.init_value_from_nested_json(json_comment_data, "author", "self")
		comment_body = JsonJiraIssueInterface.init_value_from_json("body", json_comment_data)
		comment_creation_time = JsonJiraIssueInterface.init_value_from_json("created", json_comment_data)

		return cls(comment_rest_url, comment_id, author_name, author_key, author_display_name, author_rest_url, comment_body, comment_creation_time)

	@property
	def author(self):
		return self.__author

	def __str__(self):
		return "Comment:(url: {}, id: {}, author: {}, body: {}, created: {})"\
			.format(self.__comment_rest_url, self.__comment_id, self.__author, self.__comment_body, self.__comment_creation_time)

	def __repr__(self):
		return self.__str__()
