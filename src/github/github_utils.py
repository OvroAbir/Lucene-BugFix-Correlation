from github import Github
import time
from src.common.file_utils import FileUtil


class GitHubAuth:
	@staticmethod
	def _get_auth_info():
		auth_str = FileUtil.read_file("../data/github_auth.txt")
		if auth_str == "":
			print("Github Auth tokens is not found. Program might not be able to fetch data from Github")
			print("Add github username and password in data/github_auth.txt file separated by space")
			return None, None
		return auth_str.split()[0], auth_str.split()[1]


class GitHubUtil:
	__username, __password = GitHubAuth._get_auth_info()
	__github = Github(__username, __password)
	__org = __github.get_organization('apache')
	__repo = __org.get_repo('lucene-solr')

	@staticmethod
	def __is_commit_stats_equal(commit1, commit2):
		if len(commit1.files) != len(commit2.files):
			return False
		if commit1.stats.additions != commit2.stats.additions:
			return False
		if commit1.stats.deletions != commit2.stats.deletions:
			return False
		return True

	@staticmethod
	def __get_unique_commits(commit_hashes):
		unique_commits = []
		if len(commit_hashes) == 0:
			return unique_commits

		unique_commits.append(GitHubUtil.__repo.get_commit(commit_hashes[0]))
		time.sleep(.1)
		for hash in commit_hashes[1:]:
			commit = GitHubUtil.__repo.get_commit(hash)
			time.sleep(.1)
			added_already = False
			for uniq_comt in unique_commits:
				if GitHubUtil.__is_commit_stats_equal(commit, uniq_comt):
					added_already = True
					break
			if not added_already:
				unique_commits.append(commit)
		return unique_commits

	@staticmethod
	def get_num_of_files_lines_changed_from_commit_hashes(commit_hashes):
		num_of_lines_deleted = 0
		num_of_lines_added = 0
		changed_files_names = set()

		try:
			commits = GitHubUtil.__get_unique_commits(commit_hashes)
			for commit in commits:
				for file in commit.files:
					changed_files_names.add(file.filename)
				num_of_lines_added = num_of_lines_added + commit.stats.additions
				num_of_lines_deleted = num_of_lines_deleted + commit.stats.deletions
			return len(changed_files_names), num_of_lines_deleted + num_of_lines_added
		except Exception as e:
			print(e)
			print("hashes were", commit_hashes)
			return 0, 0

	@staticmethod
	def __get_pull_request_id(pull_url):
		index = pull_url.rfind("/")
		return int(pull_url[index + 1:])

	@staticmethod
	def get_num_of_files_lines_changed_from_pull_request(pull_url):
		if pull_url is None:
			return 0, 0
		try:
			pull_id = GitHubUtil.__get_pull_request_id(pull_url)
			pull_request = GitHubUtil.__repo.get_pull(pull_id)
			time.sleep(.1)

			return pull_request.changed_files, pull_request.additions + pull_request.deletions
		except Exception as e:
			print(e)
			print("pull url was", pull_url)
			return 0, 0
