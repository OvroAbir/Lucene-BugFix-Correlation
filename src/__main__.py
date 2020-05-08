from src.jira.jira import Jira
from src.jira.jira_rest_request import JiraRestRequest
from src.processing.matplot_utils import MatPlotUtil
from src.processing.scipy_utils import SciPyUtil

from matplotlib import pyplot as plt
from scipy.stats import norm
import matplotlib.mlab as mlab
import numpy as np

jira_urls, json_filenames = JiraRestRequest.get_jira_rest_urls_and_filenames()
jira = Jira(jira_urls, json_filenames)
MatPlotUtil.plot_jira_data(jira.num_of_contributors, jira.resolve_times, jira.close_times,
						   jira.fix_times, jira.num_of_changed_files, jira.num_of_changed_lines)

# print("total", len(jira.resolve_times))
# SciPyUtil.is_normally_distributed(jira.resolve_times)

# dic = MatPlotUtil.get_2d_list_as_dictionary(jira.num_of_contributors, jira.resolve_times)
# for key in dic:
# 	print("num of contri", key)
# 	vals = dic[key]
# 	print("len is", len(vals))
# 	if len(vals) < 8:
# 		continue
# 	SciPyUtil.is_normally_distributed(vals)
#
# array = []
# for x in jira.resolve_times:
# 	array.append(x/3600/24)
# n, bins, patches = plt.hist(array, 500)
#
# weights = np.ones_like(array) / len(array)
#
# mu = np.mean(array)
# sigma = np.std(array)
# plt.plot(bins, norm.pdf(bins, mu, sigma))
# plt.show()