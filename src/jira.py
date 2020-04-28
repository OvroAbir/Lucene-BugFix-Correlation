import urllib.request, json 
from os import path, makedirs
import logging
from file_utils import File

class Jira:
    def __init__(self, query_url:str, json_filename:str="../data/unnamed-data.json", project_name:str="unnamed"):
        self.__query_url = query_url;
        self.__result_json = ""
        self.__pretty_json_str = ""
        self.__download_file_location = json_filename
        self.__download_json_if_not_exists()
        self.__project_name = project_name
 
    def __download_json_if_not_exists(self):
        filename = self.__download_file_location
        if(path.exists(filename)):
            return
        with urllib.request.urlopen(self.__query_url) as url_object:
            self.__result_json = json.loads(url_object.read().decode())
            self.__pretty_json_str = Jira.make_json_pretty(self.__result_json)
            File.write_data_to_file(filename, self.__pretty_json_str)
    
    def __delete_json(self):
        File.delete_file(self.__download_file_location)

    def __check_and_download_json(self, rewrite:bool):
        if(rewrite):
            self.__delete_json()
        self.__download_json_if_not_exists()

    def get_json_data(self, rewrite:bool=False):
        self.__check_and_download_json(rewrite)
        return self.__result_json

    def get_json_data_str(self, rewrite:bool=False):
        self.__check_and_download_json(rewrite)
        return self.__pretty_json_str



    @staticmethod
    def make_json_pretty(json_data):
        return json.dumps(json_data, indent=2, sort_keys=True)

#     def download_file_from_JQL(url:str, json_file_name:str):
#         data_json = ""
#         data_str = ""
#         with urllib.request.urlopen(url) as url_object:
#             data_json = json.loads(url_object.read().decode())
#         data_str = make_json_pretty(data_json)
#         write_json_to_file(data_str, json_file_name)
#         return data_json

# def write_json_to_file(data, filename):
#     # if(path.exists(filename) and over_Write == False):
#     #     logging.info(filename +" already exsits. Not downloading again.")
#     #     return
#     if(path.exists(path.dirname(filename)) == False):
#         makedirs(path.dirname(filename))
#     with open(filename, 'w') as f:
#         f.write(data)



