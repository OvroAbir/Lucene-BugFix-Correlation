from src.jira.jira import Jira
from src.jira.jira_rest_request import JiraRestRequest
from src.processing.matplot_utils import MatPlotUtil


def plot_data(num_of_contributors, resolve_times, close_times, fix_times,
			  num_of_changed_files, num_of_changed_lines, graph_folder):
	x_axis_datas = [num_of_contributors, num_of_changed_lines, num_of_changed_files]
	x_axis_labels = ["Number of Contributors", "Number of Changed Lines", "Number of Changed Files"]
	y_axis_datas = [resolve_times, close_times, fix_times]
	y_axis_labels = ["Resolve Time", "Closing Time", "Bug Fix Time"]
	MatPlotUtil.plot_all_data(x_axis_datas, y_axis_datas, x_axis_labels, y_axis_labels, graph_folder)

jira_url = JiraRestRequest.get_jira_rest_url("Closed", 10)
jira = Jira(jira_url, "../data/lucene-closed-data-10.json")
plot_data(jira.num_of_contributors, jira.resolve_times, jira.close_times, jira.fix_times,
		  jira.num_of_changed_files, jira.num_of_changed_lines, "../graphs")

print("jira url: ", jira_url)
