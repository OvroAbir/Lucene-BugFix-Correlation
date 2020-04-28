from jira import Jira
# def main():
#     print("Hello World");

# if(__name__ == "__main__"):
#     main()
#search for issue link

jsonfile_name = "../data/lucene-data.json"
query = "https://issues.apache.org/jira/rest/api/2/search?jql=project=LUCENE+AND+issueType=Bug&fields="
fields="id,assignee,resolution,reporter,votes,affectedVersion,fixedVersion,comment,summary,created,updated,resolved,originalEstimate,timeSpent,worklogDate,attachments,issueLinkType"

jira = Jira(query+fields, jsonfile_name, "LUCENE")
print(jira.get_json_data_str())
