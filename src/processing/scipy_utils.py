from scipy import stats
from scipy.stats import kurtosis, skew, spearmanr
from src.processing.matplot_utils import MatPlotUtil
from src.common.time_utils import TimeUtil


class SciPyUtil:
	@staticmethod
	def __concat_list_by_row(row1, row2):
		return [row1, row2]

	@staticmethod
	def __concat_list_by_column(col1, col2):
		list = []
		for i in range(len(col1)):
			row = [col1[i], col2[i]]
			list.append(row)
		return list

	@staticmethod
	def __is_normally_distributed(data):
		return stats.normaltest(data)

	@staticmethod
	def __check_normal_test(jira):
		print("Normal test of Number of contributors:", SciPyUtil.__is_normally_distributed(jira.num_of_contributors))
		print("Normal test of Resolve times:", SciPyUtil.__is_normally_distributed(jira.resolve_times))
		print("Normal test of Closing times:", SciPyUtil.__is_normally_distributed(jira.close_times))
		print("Normal test of Buf Fix times:", SciPyUtil.__is_normally_distributed(jira.fix_times))
		print("Normal test of Number of files changed:", SciPyUtil.__is_normally_distributed(jira.num_of_changed_files))
		print("Normal test of Number of lines changed:", SciPyUtil.__is_normally_distributed(jira.num_of_changed_lines))

	@staticmethod
	def __get_skew_kurtosis(data):
		return skew(data), kurtosis(data)

	@staticmethod
	def __determine_skew_and_kurtosis(jira):
		print("Skew, Kurtosis for Number of contributors:", SciPyUtil.__get_skew_kurtosis(jira.num_of_contributors))
		print("Skew, Kurtosis for Resolve times:", SciPyUtil.__get_skew_kurtosis(jira.resolve_times))
		print("Skew, Kurtosis for Closing times:", SciPyUtil.__get_skew_kurtosis(jira.close_times))
		print("Skew, Kurtosis for Buf Fix times:", SciPyUtil.__get_skew_kurtosis(jira.fix_times))
		print("Skew, Kurtosis for Number of files changed:", SciPyUtil.__get_skew_kurtosis(jira.num_of_changed_files))
		print("Skew, Kurtosis for Number of lines changed:", SciPyUtil.__get_skew_kurtosis(jira.num_of_changed_lines))

	@staticmethod
	def __plot_histograms(jira):
		MatPlotUtil.plot_histogram(jira.num_of_contributors, "Number of Contributors", "Number of Issues",
								   "../graphs/normal/histograms/NumberOfContributors.png", bins=30)
		MatPlotUtil.plot_histogram(jira.num_of_changed_files, "Number of Changed Files", "Number of Issues",
								   "../graphs/normal/histograms/NumberOfChangedFiles.png")
		MatPlotUtil.plot_histogram(jira.num_of_changed_lines, "Number of Changed Lines", "Number of Issues",
								   "../graphs/normal/histograms/NumberOfChangedLines.png")
		MatPlotUtil.plot_histogram(jira.resolve_times, "Resolve Time(second)", "Number of Issues",
								   "../graphs/normal/histograms/ResolveTime.png", bins=40)
		MatPlotUtil.plot_histogram(jira.close_times, "Closing Time(second)", "Number of Issues",
								   "../graphs/normal/histograms/ClosingTime.png", bins=40)
		MatPlotUtil.plot_histogram(jira.fix_times, "Bug Fix Time(second)", "Number of Issues",
								   "../graphs/normal/histograms/FixTime.png", bins=40)
		# MatPlotUtil.plot_histogram(TimeUtil.convert_seconds_to_hours(jira.resolve_times), "Resolve Time(hours)", "Number of Issues",
		# 						   "../graphs/normal/histograms/ResolveTimeHours.png")
		# MatPlotUtil.plot_histogram(TimeUtil.convert_seconds_to_days(jira.resolve_times), "Resolve Time(days)", "Number of Issues",
		# 						   "../graphs/normal/histograms/ResolveTimeDays.png")

	@staticmethod
	def __spearman_corelation(data1, data2):
		return spearmanr(data1, data2)

	@staticmethod
	def __check_spearman_correlation(jira):
		print("Spearman correlation for Resolve time and number of contributors:",
			  SciPyUtil.__spearman_corelation(jira.resolve_times, jira.num_of_contributors))
		print("Spearman correlation for Close time and number of contributors:",
			  SciPyUtil.__spearman_corelation(jira.close_times, jira.num_of_contributors))
		print("Spearman correlation for Bug Fix time and number of contributors:",
			  SciPyUtil.__spearman_corelation(jira.fix_times, jira.num_of_contributors))
		print("Spearman correlation for Resolve time and number of changed file:",
			  SciPyUtil.__spearman_corelation(jira.resolve_times, jira.num_of_changed_files))
		print("Spearman correlation for Close time and number of changed file:",
			  SciPyUtil.__spearman_corelation(jira.close_times, jira.num_of_changed_files))
		print("Spearman correlation for Bug Fix time and number of changed file:",
			  SciPyUtil.__spearman_corelation(jira.fix_times, jira.num_of_changed_files))
		print("Spearman correlation for Resolve time and number of changed lines:",
			  SciPyUtil.__spearman_corelation(jira.resolve_times, jira.num_of_changed_lines))
		print("Spearman correlation for Close time and number of changed lines:",
			  SciPyUtil.__spearman_corelation(jira.close_times, jira.num_of_changed_lines))
		print("Spearman correlation for Bug Fix time and number of changed lines:",
			  SciPyUtil.__spearman_corelation(jira.fix_times, jira.num_of_changed_lines))

	@staticmethod
	def check_jira_data_normal_distribution(jira):
		SciPyUtil.__check_normal_test(jira)
		SciPyUtil.__determine_skew_and_kurtosis(jira)
		SciPyUtil.__plot_histograms(jira)
		SciPyUtil.__check_spearman_correlation(jira)
