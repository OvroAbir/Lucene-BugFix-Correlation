from src.jira.jira_user import User
from src.common.json_interface import Json_Jira_Issue_Interface
import urllib.request


class Jira_Attachment:
	def __init__(self, attachment_id, attachment_filename,
				 attachment_author_name, attachment_author_key, attachment_author_display_name, attachment_author_url,
				 attachment_size, attachment_created, attachment_content_url, mime_type):
		self.__attachment_id = attachment_id
		self.__attachment_filename = attachment_filename
		self.__author = User(attachment_author_name, attachment_author_key, attachment_author_display_name,
							 attachment_author_url)
		self.__attachment_size = attachment_size
		self.__attachment_created = attachment_created
		self.__attachment_content_url = attachment_content_url
		self.__attachment_mime_type = mime_type

	@property
	def author(self):
		return self.__author

	@property
	def attachment_content_url(self):
		return self.__attachment_content_url

	def get_attachment_content(self):
		if not self.is_attachment_text_file():
			raise Exception("Attachment is not text file. Attachment type is {}".format(self.__attachment_mime_type))
		attachment_url = self.__attachment_content_url
		attachment_content = ""
		with urllib.request.urlopen(attachment_url) as content:
			attachment_content = content.read().decode(errors='ignore')
		return attachment_content

	def is_attachment_text_file(self):
		if self.__attachment_mime_type.startswith('text'):
			return True

	@classmethod
	def get_object_from_json(cls, json_obj):
		attachment_id = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "id")
		attachment_filename = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "filename")
		attachment_authorname = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "author", "name")
		attachment_author_key = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "author", "key")
		attachment_author_display_name = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "author",
																							   "displayName")
		attachment_author_url = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "author", "self")
		attachment_size = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "size")
		attachment_created = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "created")
		attachment_content = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "content")
		mime_type = Json_Jira_Issue_Interface.init_value_from_nested_json(json_obj, "mimeType")

		return cls(attachment_id, attachment_filename,
				   attachment_authorname, attachment_author_key, attachment_author_display_name, attachment_author_url,
				   attachment_size, attachment_created, attachment_content, mime_type)
