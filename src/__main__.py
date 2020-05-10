from src.jira.jira import Jira
from src.jira.jira_rest_request import JiraRestRequest
from src.processing.matplot_utils import MatPlotUtil
from src.processing.scipy_utils import SciPyUtil


def main():
	jira_urls, json_filenames = JiraRestRequest.get_jira_rest_urls_and_filenames()
	jira = Jira(jira_urls, json_filenames)
	MatPlotUtil.plot_jira_data(jira.num_of_contributors, jira.resolve_times, jira.close_times,
							   jira.fix_times, jira.num_of_changed_files, jira.num_of_changed_lines)
	print(jira_urls)
	print(SciPyUtil.check_jira_data_normal_distribution(jira))


if __name__ == "__main__":
	main()
