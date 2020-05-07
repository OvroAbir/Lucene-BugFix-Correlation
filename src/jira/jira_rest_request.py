class JiraRestRequest:
	@staticmethod
	def __make_jql_args(issue_status, number_of_issues, start):
		arguments = {
			"baseurl": "https://issues.apache.org/jira/rest/api/2/search?jql=",
			"project": "LUCENE",
			"issueType": "Bug",
			"maxResults": str(number_of_issues),
			"startAt": str(start),
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
			]
		}
		return arguments

	@staticmethod
	def __construct_jql_url(arguments):
		url = ""
		url = url + arguments["baseurl"];
		if "project" in arguments:
			url = url + "project=" + arguments["project"] + "+AND+"
		if "issueType" in arguments:
			url = url + "issueType=" + arguments["issueType"] + "+AND+"
		if "status" in arguments:
			url = url + "status=" + arguments["status"] + "&"
		if "maxResults" in arguments:
			url = url + "maxResults=" + arguments["maxResults"] + "&"
		if "startAt" in arguments:
			url = url + "startAt=" + arguments["startAt"] + "&"
		url = url + "expand=changelog"+ "&"
		if "fields" in arguments:
			url = url + "fields="
			for field in arguments["fields"]:
				url = url + field + ","
		url = url[:-1]
		return url

	@staticmethod
	def get_one_jira_rest_url(issue_status, number_of_issues, start=0):
		return JiraRestRequest.__construct_jql_url(JiraRestRequest.__make_jql_args(issue_status, number_of_issues, start))

	@staticmethod
	def get_jira_rest_urls_and_filenames():
		jira_urls = []
		file_names = []
		start = 0
		max_results = 1000
		while start < 3000:
			url = JiraRestRequest.get_one_jira_rest_url("Closed", max_results, start)
			filename = "../data/lucene-closed-data-3400-from-" + str(start) + ".json"
			jira_urls.append(url)
			file_names.append(filename)
			start = start + max_results

		return jira_urls, file_names
