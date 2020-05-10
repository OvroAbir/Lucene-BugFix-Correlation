from git import Repo


class GitHubUtil:
	__repo = Repo("../data/lucene-solr")

	@staticmethod
	def change_repo(new_repo_path):
		GitHubUtil.__repo = Repo(new_repo_path)

	@staticmethod
	def get_num_of_files_lines_changed_from_commit_hash(commit_hash):
		commit = GitHubUtil.__repo.commit(commit_hash)
		stats = commit.stats.total
		return stats['files'], stats['lines']