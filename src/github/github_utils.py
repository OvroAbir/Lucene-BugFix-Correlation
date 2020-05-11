from github import Github


class GitHubUtil:
	__github = Github()
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
		for hash in commit_hashes[1:]:
			commit = GitHubUtil.__repo.get_commit(hash)
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

		commits = GitHubUtil.__get_unique_commits(commit_hashes)
		for commit in commits:
			for file in commit.files:
				changed_files_names.add(file.filename)
			num_of_lines_added = num_of_lines_added + commit.stats.additions
			num_of_lines_deleted = num_of_lines_deleted + commit.stats.deletions

		return len(changed_files_names), num_of_lines_deleted+num_of_lines_added

	@staticmethod
	def __get_pull_request_id(pull_url):
		index = pull_url.rfind("/")
		return int(pull_url[index+1:])

	@staticmethod
	def get_num_of_files_lines_changed_from_pull_request(pull_url):
		if pull_url is None:
			return 0, 0
		pull_id = GitHubUtil.__get_pull_request_id(pull_url)
		pull_request = GitHubUtil.__repo.get_pull(pull_id)

		return pull_request.changed_files, pull_request.additions+pull_request.deletions


