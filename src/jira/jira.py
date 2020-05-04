import urllib.request, json
from os import path
from src.common.file_utils import FileUtil
from src.common.urllib_utils import UrlLibUtil
from src.jira.jira_issue import JiraIssue
from src.common.json_interface import JsonJiraIssueInterface
from src.common.json_pickle_utils import JsonPickleUtil


class Jira:
	def __init__(self, query_url: str, jira_json_filename: str = "../data/unnamed-data.json"):
		self.__query_url = query_url
		self.__jira_file_location = jira_json_filename
		self.__self_file_location = self.__get_self_file_location()
		self.__issue_list = self.__get_inited_issue_list()
		self.__save_issue_list_to_self_file()

	def __get_inited_issue_list(self):
		if self.__does_self_file_exists():
			return JsonPickleUtil.get_obj_from_str(self.__get_self_json())
		else:
			json_str = self.__download_and_load__jira_json_str_if_not_exists()
			return self.__extract_issues_from_json(json_str)

	def __save_issue_list_to_self_file(self):
		json_pickle = JsonPickleUtil.get_str_from_obj(self.__issue_list)
		FileUtil.write_data_to_file(self.__self_file_location, json_pickle)

	@property
	def issue_list(self):
		return self.__issue_list

	def __does_self_file_exists(self):
		return path.exists(self.__self_file_location)

	def __get_self_file_location(self):
		return FileUtil.add_str_to_filename(self.__jira_file_location, "_self")

	def __get_self_json(self):
		if path.exists(self.__self_file_location):
			print("Reading from self json file")
			json_str = FileUtil.read_file(self.__self_file_location)
			return json_str
		return "null"

	def __download_and_load__jira_json_str_if_not_exists(self):
		filename = self.__jira_file_location
		if path.exists(filename):
			return FileUtil.read_file(filename)
		result_json = UrlLibUtil.download_and_parse_json(self.__query_url)
		pretty_json_str = Jira.make_json_pretty(result_json)
		FileUtil.write_data_to_file(filename, pretty_json_str)
		return pretty_json_str

	def __extract_issues_from_json(self, jira_json_str):
		jira_issues = []
		jira_json_obj = json.loads(jira_json_str)
		issues_json = JsonJiraIssueInterface.init_value_from_json("issues", jira_json_obj)
		for issue_json in issues_json:
			jira_issues.append(JiraIssue(issue_json))
		return jira_issues

	@staticmethod
	def make_json_pretty(json_data):
		return json.dumps(json_data, indent=2, sort_keys=True)
