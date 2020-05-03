import jsonpickle


class JsonPickleUtil:
	@staticmethod
	def get_str_from_obj(obj):
		return jsonpickle.encode(obj)

	@staticmethod
	def get_obj_from_str(obj_str):
		return jsonpickle.decode(obj_str)
