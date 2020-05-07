from src.jira.jira_fraction import JiraFraction
from typing import List


class Jira:
	def __init__(self, query_list:List[str], jira_json_filenames:List[str]):
		self.__jira_fractions = self.__generate_jira_fractions(query_list, jira_json_filenames)

	def __generate_jira_fractions(self, query_list, jira_json_filenames):
		fractions = []
		for i in range(len(query_list)):
			jira_fraction = JiraFraction(query_list[i], jira_json_filenames[i])
			fractions.append(jira_fraction)
		return fractions

	@property
	def issue_list(self):
		issue_list = []
		for jira_fraction in self.__jira_fractions:
			issue_list = issue_list + jira_fraction.issue_list
		return issue_list

	@property
	def issue_keys(self):
		keys = []
		for jira_fraction in self.__jira_fractions:
			keys = keys + jira_fraction.issue_keys
		return keys

	@property
	def fix_times(self):
		times = []
		for jira_fraction in self.__jira_fractions:
			times = times + jira_fraction.fix_times
		return times

	@property
	def close_times(self):
		times = []
		for jira_fraction in self.__jira_fractions:
			times = times + jira_fraction.close_times
		return times

	@property
	def resolve_times(self):
		times = []
		for jira_fraction in self.__jira_fractions:
			times = times + jira_fraction.resolve_times
		return times

	@property
	def num_of_contributors(self):
		nums = []
		for jira_fraction in self.__jira_fractions:
			nums = nums + jira_fraction.num_of_contributors
		return nums

	@property
	def num_of_changed_files(self):
		nums = []
		for jira_fraction in self.__jira_fractions:
			nums = nums + jira_fraction.num_of_changed_files
		return nums

	@property
	def num_of_changed_lines(self):
		nums = []
		for jira_fraction in self.__jira_fractions:
			nums = nums + jira_fraction.num_of_changed_lines
		return nums