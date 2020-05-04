from os import path, makedirs, remove
import logging

class File:
	@staticmethod
	def write_data_to_file(filename, data):
		if(path.exists(path.dirname(filename)) == False):
			makedirs(path.dirname(filename))
		print("Writing data to " + filename)
		with open(filename, 'w') as f:
			f.write(data)
	
	@staticmethod
	def delete_file(filename):
		print("Deleting file " + filename)
		if(path.isfile(filename)):
			remove(filename)

	@staticmethod
	def read_file(filename):
		if(path.isfile(filename) == False):
			print("File {} does not exist".format(filename))
			return ""
		data =""
		with open(filename, 'r') as f:
			data = f.read()
		return data

	@staticmethod
	def add_str_to_filename(filename, new_str):
		old_filename, extension = path.splitext(filename)
		new_filename = old_filename + new_str
		return new_filename + extension