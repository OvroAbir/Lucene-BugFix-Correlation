from unidiff import PatchSet


class FilesChangedNumber:

	@staticmethod
	def get_num_files_changed(issue):
		try:
			diff = issue
			patch = PatchSet(diff)
			return len(patch)
		except Exception as e:
			print(e)
			return 0

	@staticmethod
	def get_num_lines_changed(issue):
		try:
			diff = issue
			patch = PatchSet(diff)
			count = []
			for p in patch:
				num = p.added + p.removed
				if num is not None:
					count.append(num)
			return sum(count)
		except Exception as e:
			print(e)
			return 0
