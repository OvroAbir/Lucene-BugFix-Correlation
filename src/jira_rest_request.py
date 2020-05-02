class Jira_Rest_Request:
	@staticmethod
	def __make_jql_agrs(issue_status, number_of_issues):
		arguments = {
			"baseurl": "https://issues.apache.org/jira/rest/api/2/search?jql=",
			"project": "LUCENE",
			"issueType": "Bug",
			"maxResults": str(number_of_issues),
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

	@staticmethod
	def __construct_jql_url(arguments):
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

	@staticmethod
	def get_jira_rest_url(issue_status, number_of_issues):
		return Jira_Rest_Request.__construct_jql_url(Jira_Rest_Request.__make_jql_agrs(issue_status, number_of_issues))
