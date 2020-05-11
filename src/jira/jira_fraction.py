import json
import time
from os import path
from src.common.file_utils import FileUtil
from src.common.json_interface import JsonJiraIssueInterface
from src.common.json_pickle_utils import JsonPickleUtil
from src.common.urllib_utils import UrlLibUtil
from src.jira.jira_issue import JiraIssue


class JiraFraction:
	def __init__(self, query_url: str, jira_json_filename: str = "../data/unnamed-data.json"):
		print("Started parsing fraction" + jira_json_filename)
		self.__query_url = query_url
		self.__jira_file_location = jira_json_filename
		self.__self_file_location = self.__get_self_file_location()
		self.__issue_list = self.__get_inited_issue_list()
		self.__save_issue_list_to_self_file()
		print("Ended parsing fraction" + jira_json_filename)

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
		print("Downloading data to " + filename + " ...")
		result_json = UrlLibUtil.download_and_parse_json(self.__query_url)
		pretty_json_str = JiraFraction.make_json_pretty(result_json)
		FileUtil.write_data_to_file(filename, pretty_json_str)
		return pretty_json_str

	def __extract_issues_from_json(self, jira_json_str):
		jira_issues = []
		jira_json_obj = json.loads(jira_json_str)
		issues_json = JsonJiraIssueInterface.init_value_from_json("issues", jira_json_obj)

		for issue_json in issues_json:
			try_count = 0
			success = False
			while success is False and try_count < 2:
				try:
					jira_issue_obj = JiraIssue(issue_json)
					if jira_issue_obj.number_of_files_changed != 0 or jira_issue_obj.number_of_lines_changed != 0:
						jira_issues.append(jira_issue_obj)
					else:
						print("Not appending ", jira_issue_obj.data.issue_key)
					success = True
				except Exception as e:
					print(e)
					print("Failed parsing issue.")
					try_count = try_count + 1
					time.sleep(5)

		return jira_issues

	@staticmethod
	def make_json_pretty(json_data):
		return json.dumps(json_data, indent=2, sort_keys=True)

	@property
	def issue_keys(self):
		keys = []
		for issue in self.__issue_list:
			keys.append(issue.data.issue_key)
		return keys

	@property
	def fix_times(self):
		times = []
		for issue in self.__issue_list:
			times.append(issue.fix_time)
		return times

	@property
	def close_times(self):
		times = []
		for issue in self.__issue_list:
			times.append(issue.close_time)
		return times

	@property
	def resolve_times(self):
		times = []
		for issue in self.__issue_list:
			times.append(issue.resolve_time)
		return times

	@property
	def num_of_contributors(self):
		nums = []
		for issue in self.__issue_list:
			nums.append(issue.contributors_number)
		return nums

	@property
	def num_of_changed_files(self):
		nums = []
		for issue in self.__issue_list:
			nums.append(issue.number_of_files_changed)
		return nums

	@property
	def num_of_changed_lines(self):
		nums = []
		for issue in self.__issue_list:
			nums.append(issue.number_of_lines_changed)
		return nums
