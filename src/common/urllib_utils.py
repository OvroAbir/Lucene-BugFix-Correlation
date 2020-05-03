import urllib.request
import json


class UrlLibUtil:
	@staticmethod
	def download_content(url):
		with urllib.request.urlopen(url) as url_object:
			result_json = url_object.read()
			return result_json

	@staticmethod
	def download_and_parse_json(url):
		content = UrlLibUtil.download_content(url)
		return json.loads(content.decode())
