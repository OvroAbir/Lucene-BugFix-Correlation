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
