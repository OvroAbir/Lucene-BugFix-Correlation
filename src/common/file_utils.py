from os import path, makedirs, remove


class FileUtil:
	@staticmethod
	def create_directory_if_not_exists(directory_name):
		makedirs(directory_name, exist_ok=True)

	@staticmethod
	def write_data_to_file(filename, data):
		if not path.exists(path.dirname(filename)):
			makedirs(path.dirname(filename))
		print("Writing data to " + filename)
		with open(filename, 'w') as f:
			f.write(data)

	@staticmethod
	def delete_file(filename):
		print("Deleting file " + filename)
		if path.isfile(filename):
			remove(filename)

	@staticmethod
	def read_file(filename):
		if not path.isfile(filename):
			print("File {} does not exist".format(filename))
			return ""
		data = ""
		with open(filename, 'r') as f:
			data = f.read()
		return data

	@staticmethod
	def add_str_to_filename(filename, new_str):
		old_filename, extension = path.splitext(filename)
		new_filename = old_filename + new_str
		return new_filename + extension

	@staticmethod
	def concat_filename_with_path(parent_path, filename):
		return path.join(parent_path, filename)
