from src.jira.jira import Jira
from src.jira.jira_rest_request import Jira_Rest_Request


jira_url = Jira_Rest_Request.get_jira_rest_url("Closed", 10)
jira = Jira(jira_url, "../data/lucene-closed-data-10.json", "lucene")

# for issue in jira.issue_list:
# 	print(issue.data.issue_key, issue.contributors_number)

print("jira url: ", jira_url)
# print("Jira Object:", jira)