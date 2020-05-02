from .jira import Jira
# def main():
#     print("Hello World");

# if(__name__ == "__main__"):
#     main()
#search for issue link

def make_jql_agrs(issue_status):
	arguments = {
		"baseurl": "https://issues.apache.org/jira/rest/api/2/search?jql=",
		"project": "LUCENE",
		"issueType": "Bug",
		"maxResults": "10",
		"status": issue_status,
		"fields": [
			"id",
			"self",
			"key",
			"priority",
			"assignee",
			"status",
			"creator",
			"reporter",
			"issuetype",
			"project",
			"created",
			"description",
			"timetracking",
			"summary",
			"comment",
			"attachment",

			"affectedVersion",
			"fixedVersion",
			"resolved",
			"timeSpent",
			# "issueLinkType"
		]
	}
	return arguments
def construct_jql_url(arguments):
	url = ""
	url = url + arguments["baseurl"];
	if("project" in arguments):
		url = url + "project=" + arguments["project"] + "+AND+"
	if("issueType" in arguments):
		url = url + "issueType=" + arguments["issueType"] + "+AND+"
	if("status" in arguments):
		url = url + "status=" + arguments["status"] + "&"
	if("maxResults" in arguments):
		url = url + "maxResults=" + arguments["maxResults"] + "&"
	if("fields" in arguments):
		url = url + "fields="
		for field in arguments["fields"]:
			url = url + field + ","
	url = url[:-1]
	return url

# query1 = construct_jql_url(make_jql_agrs("closed"))
# query2 = construct_jql_url(make_jql_agrs("resolved"))



# jsonfile_name1 = "../data/lucene-closed-data-10.json"
# jsonfile_name2 = "../data/lucene-resolved-data-50.json"

# https://issues.apache.org/jira/rest/api/2/search?jql=project=LUCENE+AND+issueType=Bug&maxResults=1000&fields="
# fields="id,assignee,resolution,reporter,votes,affectedVersion,fixedVersion,comment,summary,created,updated,resolved,originalEstimate,timeSpent,worklogDate,attachments,issueLinkType"

# jira1 = Jira(query1, jsonfile_name1, "LUCENE")
# json_data1 = jira1.get_json_data()

# jira2 = Jira(query2, jsonfile_name2, "LUCENE")
# json_data2 = jira2.get_json_data()


# print(len(json_data1["issues"]))
# print(len(json_data2["issues"]))
