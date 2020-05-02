from .jira import Jira
from .jira_rest_request import Jira_Rest_Request


jira_url = Jira_Rest_Request.get_jira_rest_url("Closed", 10)
print(jira_url)
# jira = Jira(jira_url, "../data/lucene-closed-data-10.json", "lucene")
