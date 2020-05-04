from src.common.json_interface import JsonJiraIssueInterface


class JiraIssueRemoteLink:
	def __init__(self, link_str, link_title):
		self.__link = link_str
		self.__title = link_title

	@property
	def link(self):
		return self.__link

	@property
	def title(self):
		return self.__title

	def __str__(self):
		return "(" + self.__link + ", " + self.__title + ")"

	def __repr__(self):
		return self.__str__()

	@classmethod
	def get_object_from_json(cls, json_remote_link_data):
		link = JsonJiraIssueInterface.init_value_from_nested_json(json_remote_link_data, "object", "url")
		title = JsonJiraIssueInterface.init_value_from_nested_json(json_remote_link_data, "object", "title")
		return cls(link, title)
