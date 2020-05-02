import urllib.request, json
from os import path, makedirs
from .file_utils import File
from .jira_issue import Jira_Issue_Data
from .json_interface import Json_Jira_Issue_Interface


class Jira:
	def __init__(self, query_url: str, json_filename: str = "../data/unnamed-data.json", project_name: str = "unnamed"):
		self.__query_url = query_url;
		self.__result_json = ""
		self.__pretty_json_str = ""
		self.__download_file_location = json_filename
		self.__project_name = project_name
		self.__download_and_load_json_if_not_exists()
		self.__issue_list = self.__extract_issues_from_json()

	def __download_and_load_json_if_not_exists(self):
		filename = self.__download_file_location
		if (path.exists(filename)):
			self.__load_json_from_file()
			return
		with urllib.request.urlopen(self.__query_url) as url_object:
			self.__result_json = json.loads(url_object.read().decode())
			self.__pretty_json_str = Jira.make_json_pretty(self.__result_json)
			File.write_data_to_file(filename, self.__pretty_json_str)

	def __delete_json(self):
		File.delete_file(self.__download_file_location)

	def __load_json_from_file(self):
		print("loading file")
		self.__pretty_json_str = File.read_file(self.__download_file_location)
		self.__result_json = json.loads(self.__pretty_json_str)

	def __check_and_download_json(self, rewrite: bool):
		if rewrite:
			self.__delete_json()
		self.__download_and_load_json_if_not_exists()

	def rewrite_json_data(self):
		self.__check_and_download_json(True)

	def get_json_data(self, rewrite: bool = False):
		return self.__result_json

	def get_json_data_str(self):
		return self.__pretty_json_str

	def __extract_issues_from_json(self):
		jira_issues = []
		issues_json = Json_Jira_Issue_Interface.init_value_from_json("issues", self.__result_json)
		for issue_json in issues_json:
			jira_issues.append(Jira_Issue_Data(issue_json))
		return jira_issues

	@staticmethod
	def make_json_pretty(json_data):
		return json.dumps(json_data, indent=2, sort_keys=True)
