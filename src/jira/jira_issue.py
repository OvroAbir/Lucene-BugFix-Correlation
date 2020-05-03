from src.jira.jira_issue_data import Jira_Issue_Data
from src.common.time import TimeUtil


class Jira_Issue:
	def __init__(self, json_data):
		self.__data = Jira_Issue_Data(json_data)
		self.__resolve_time, self.__close_time = self.__calculate_fix_times()
		self.__contributors_number = self.__calculate_contributors_number()

	@property
	def resolve_time(self):
		return self.__resolve_time

	@property
	def close_time(self):
		return self.__close_time

	@property
	def contributors_number(self):
		return self.__contributors_number

	@property
	def data(self):
		return self.__data

	def __calculate_contributors_number(self):
		issue_comments = self.__data.comments
		issue_attachments = self.__data.attachments
		commenter_set = self.__get_commentors_set(issue_comments)
		attacher_set = self.__get_attachers_set(issue_attachments)
		contributor_set = commenter_set.union(attacher_set)

		if self.__data.assignee is not None:
			contributor_set.add(self.__data.assignee.key)
		if self.__data.creator is not None:
			contributor_set.add(self.__data.creator.key)
		if self.__data.reporter is not None:
			contributor_set.add(self.__data.reporter.key)

		contributor_set.discard('jira-bot')
		return len(contributor_set)

	def __get_commentors_set(self, comments):
		user_set = set()
		for comment in comments:
			author = comment.author
			user_set.add(author.key)
		return user_set

	def __get_attachers_set(selfself, attachments):
		user_set = set()
		for attachment in attachments:
			author = attachment.author
			user_set.add(author.key)
		return user_set

	def __calculate_fix_times(self):
		issue_history = self.__data.changelog
		issue_creation_time = self.__data.created
		status_event_times = self.__get_all_event_times(issue_history)
		resolve_time, closed_time = self.__calculate_resolve_and_closing_time(issue_creation_time,
																			  status_event_times)
		return resolve_time, closed_time

	def __calculate_resolve_and_closing_time(self, creation_time, status_event_times):
		resolved_time = 0
		closed_time = 0
		from_time = creation_time

		for (time, from_event, to_event) in status_event_times:
			if to_event == 'Resolved':
				resolved_time = resolved_time + TimeUtil.get_time_diff(from_time, time)
				from_time = time
			elif to_event == 'Closed':
				closed_time = TimeUtil.get_time_diff(from_time, time)
				from_time = time
			elif closed_time != 0:
				resolved_time = resolved_time + closed_time
				closed_time = 0
				from_time = time
		return resolved_time, closed_time

	def __get_all_event_times(self, histories):
		status_event_times = []
		for history in histories:
			for item in history.items:
				if item.field == 'status':
					status_event_times.append((history.created_time, item.from_str, item.to_str))
		return status_event_times
