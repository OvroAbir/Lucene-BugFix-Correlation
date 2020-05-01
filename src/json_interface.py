import json

class Json_Jira_Issue_Interface:

	@staticmethod
	def init_value_from_json(key, json_obj):
		if key in json_obj:
			return json_obj[key]
		return ""

	@staticmethod
	def init_value_from_nested_json(json_obj, *key_levels):
		level_json_obj = json_obj
		for key_level in key_levels:
			if key_level not in level_json_obj:
				return ""
			level_json_obj = level_json_obj[key_level]
		return level_json_obj

	@staticmethod
	def init_array_from_json(json_obj, cls_ref, *key_levels):
		key_level_len = len(key_levels)
		level_json_obj = json_obj
		object_list = []
		for level in range(key_level_len-1):
			if key_levels[level] not in level_json_obj:
				return []
			level_json_obj = level_json_obj[key_levels[level]]

		max_result = level_json_obj["maxResults"]
		cls_objs = level_json_obj[key_levels[key_level_len-1]]
		for i in range(max_result):
			object_list.append(cls_ref.get_object_from_json(cls_objs[i]))
		return object_list

	@staticmethod
	def init_object_from_nested_json(json_obj, cls_ref, *key_levels):
		level_json_obj = json_obj
		for key_level in key_levels:
			if key_level not in level_json_obj:
				return ""
			level_json_obj = level_json_obj[key_level]
		return cls_ref.get_object_from_json(level_json_obj)