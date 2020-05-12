from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator, LinearLocator
from src.common.file_utils import FileUtil
from statistics import median


class MatPlotUtil:
	@staticmethod
	def pointplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
		plt.style.use('ggplot')
		fig, ax = plt.subplots()
		ax.plot(x, y, linewidth=0, marker='s', label=point_label)
		ax.set_xlabel(x_axis_name)
		ax.set_ylabel(y_axis_name)
		ax.legend(facecolor='white')
		ax.xaxis.set_major_locator(MaxNLocator(integer=True))
		ax.set_title(graph_title)
		FileUtil.create_directory_if_not_exists(image_directory)
		plt.savefig(FileUtil.concat_filename_with_path(image_directory, graph_title + ".png"), bbox_inches='tight')
		plt.close()

	@staticmethod
	def plot_all_types_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
		MatPlotUtil.pointplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory+"/ScatterPlot", graph_title)
		MatPlotUtil.boxplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory + "/BoxPlot",
									graph_title)
		MatPlotUtil.violinplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory + "/ViolinPlot",
								 graph_title)

	@staticmethod
	def violinplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
		# plt.style.use('ggplot')
		fig, ax = plt.subplots()
		dictionary = MatPlotUtil.get_dictionary_from_two_lists(x, y)
		data = MatPlotUtil.get_dict_vals_as_2d_list(dictionary)
		labels = sorted(dictionary)

		ax.violinplot(data, showmeans=False, showmedians=True, positions=labels)
		# ax.set_xticklabels(labels=labels)
		ax.yaxis.grid(True)
		ax.set_xlabel(x_axis_name)
		ax.set_ylabel(y_axis_name)
		ax.legend(facecolor='white')
		ax.set_title(graph_title)
		FileUtil.create_directory_if_not_exists(image_directory)
		plt.savefig(FileUtil.concat_filename_with_path(image_directory, graph_title + ".png"), bbox_inches='tight')
		plt.close()

	@staticmethod
	def __get_zero_padded_strs(nums):
		max_num = max(nums)
		max_len = len(str(max_num))
		s = "{:0" + str(max_len) +"d}"
		num_strs = []
		for num in nums:
			num_strs.append(s.format(num))
		return num_strs

	@staticmethod
	def __get_labels_with_oobservation_count(x_labels, observation_counts):
		labels = []
		oc_strs = MatPlotUtil.__get_zero_padded_strs(observation_counts)
		for i in range(len(x_labels)):
			labels.append("(OC=" + oc_strs[i]+") " + str(x_labels[i]))
		return labels


	@staticmethod
	def boxplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
		# # plt.style.use('ggplot')
		fig, ax = plt.subplots()
		dictionary = MatPlotUtil.get_dictionary_from_two_lists(x, y)
		data = MatPlotUtil.get_dict_vals_as_2d_list(dictionary)
		labels = sorted(dictionary)
		observation_counts = MatPlotUtil.__get_observation_counts(dictionary)
		labels = MatPlotUtil.__get_labels_with_oobservation_count(labels, observation_counts)

		# ax2 = ax.twiny()
		# ax2.xaxis.set_minor_locator(LinearLocator())
		# # ax2.set_xlim(ax.get_xlim())
		# ax2.set_xlabel("Observation Count")
		# ax2.set_xticklabels(observation_counts)
		# print("title:", graph_title, observation_counts)
		# ax2.set_yticks(observation_counts)
		# ax2.set_labels(observation_counts)


		ax.boxplot(data, labels=labels)
		ax.yaxis.grid(True)
		ax.set_xlabel(x_axis_name)
		ax.set_ylabel(y_axis_name)
		ax.legend(facecolor='white')
		ax.set_title(graph_title)
		FileUtil.create_directory_if_not_exists(image_directory)
		# plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='left', fontsize='x-small')
		plt.setp(ax.get_xticklabels(), rotation=90, horizontalalignment='left')
		plt.savefig(FileUtil.concat_filename_with_path(image_directory, graph_title + ".png"), bbox_inches='tight')
		plt.close()

	@staticmethod
	def plot_all_data(x_axis_datas, y_axis_datas, x_axis_lables, y_axis_lables, graph_driectory):
		plt.rcParams["figure.figsize"] = [plt.rcParams["figure.figsize"][0]*2.25, plt.rcParams["figure.figsize"][1]*1.5]
		for x_index in range(len(x_axis_datas)):
			for y_index in range(len(y_axis_datas)):
				graph_title = y_axis_lables[y_index] + " vs " + x_axis_lables[x_index]
				MatPlotUtil.plot_all_types_data(x_axis_datas[x_index], y_axis_datas[y_index],
									  y_axis_lables[y_index], x_axis_lables[x_index], y_axis_lables[y_index],
									  graph_driectory, graph_title)
				# median_xs, median_ys = MatPlotUtil.convert_yaxis_to_median(x_axis_datas[x_index], y_axis_datas[y_index])
				# MatPlotUtil.boxplot_data(median_xs, median_ys,
				# 					  y_axis_lables[y_index], x_axis_lables[x_index], y_axis_lables[y_index] + " Median",
				# 					  graph_driectory, graph_title + " Median")

	@staticmethod
	def plot_jira_data(num_of_contributors, resolve_times, close_times, fix_times,
				  num_of_changed_files, num_of_changed_lines, graph_folder="../graphs"):
		x_axis_datas = [num_of_contributors, num_of_changed_lines, num_of_changed_files]
		x_axis_labels = ["Number of Contributors", "Number of Changed Lines", "Number of Changed Files"]
		y_axis_datas = [resolve_times, close_times, fix_times]
		y_axis_labels = ["Resolve Time (sec)", "Closing Time (sec)", "Bug Fix Time (sec)"]
		MatPlotUtil.plot_all_data(x_axis_datas, y_axis_datas, x_axis_labels, y_axis_labels, graph_folder)
		# MatPlotUtil.plot_partial_graph([x_axis_datas[1]], y_axis_datas, [x_axis_labels[1]], y_axis_labels, graph_folder, 120)
		MatPlotUtil.plot_grouped_graph([x_axis_datas[1]], y_axis_datas, [x_axis_labels[1]], y_axis_labels, graph_folder, 30)

	@staticmethod
	def plot_partial_graph(x_axis_datas, y_axis_datas, x_axis_lables, y_axis_lables, graph_folder, counts_of_points_to_plot):
		for x_index in range(len(x_axis_datas)):
			for y_index in range(len(y_axis_datas)):
				x_axis_data_partial, y_axis_data_partial = MatPlotUtil.__get_partail_datas_along_x_axis(x_axis_datas[x_index], y_axis_datas[y_index], counts_of_points_to_plot)
				graph_title = y_axis_lables[y_index] + " vs " + x_axis_lables[x_index] + " (partial)"
				MatPlotUtil.plot_all_types_data(x_axis_data_partial, y_axis_data_partial,
												y_axis_lables[y_index], x_axis_lables[x_index], y_axis_lables[y_index],
												graph_folder+"/partial", graph_title)

	@staticmethod
	def plot_grouped_graph(x_axis_datas, y_axis_datas, x_axis_lables, y_axis_lables, graph_folder, x_intervals_len):
		for x_index in range(len(x_axis_datas)):
			for y_index in range(len(y_axis_datas)):
				x_axis_data, y_axis_data = MatPlotUtil.__get_grouped_datas_along_x_axis(x_axis_datas[x_index], y_axis_datas[y_index], x_intervals_len)
				graph_title = y_axis_lables[y_index] + " vs " + x_axis_lables[x_index] + " (grouped)"
				MatPlotUtil.boxplot_data(x_axis_data, y_axis_data,
												y_axis_lables[y_index], x_axis_lables[x_index], y_axis_lables[y_index],
												graph_folder + "/BoxPlot", graph_title)

	@staticmethod
	def convert_yaxis_to_median(xs, ys):
		values_dict = {}
		for i in range(len(xs)):
			if xs[i] in values_dict:
				values_dict[xs[i]].append(ys[i])
			else:
				values_dict[xs[i]] = []

		new_xs = []
		new_ys = []
		for key in values_dict:
			vals = values_dict[key]
			if len(vals) == 0:
				continue
			new_xs.append(key)
			new_ys.append(median(vals))

		return new_xs, new_ys

	@staticmethod
	def get_dictionary_from_two_lists(xs, ys):
		values_dict = {}
		for i in range(len(xs)):
			if xs[i] in values_dict:
				values_dict[xs[i]].append(ys[i])
			else:
				values_dict[xs[i]] = [ys[i]]
		pruned_dictionary = MatPlotUtil.__discard_low_density_data(values_dict)
		return pruned_dictionary

	@staticmethod
	def __discard_low_density_data(dictionary): # discard keys if less than 5 value exists for this key
		# print("before dic", dictionary)
		new_dict = {}
		for key in dictionary:
			if len(dictionary[key]) >= 5:
				new_dict[key] = dictionary[key]
		# print("new dic", new_dict)
		# return dictionary
		return new_dict

	@staticmethod
	def get_dict_vals_as_2d_list(dictionary):
		values_list = list()
		for key in sorted(dictionary):
			vals = dictionary[key]
			values_list.append(vals)
		return values_list

	@staticmethod
	def plot_histogram(data, x_axis_label, y_axis_label, filename, bins=None):
		FileUtil.create_directory_if_not_exists_for_file(filename)
		plt.xlabel(x_axis_label)
		plt.ylabel(y_axis_label)
		plt.hist(data, bins=bins)
		plt.savefig(fname=filename)
		print("Saving histogram", filename)
		plt.close()

	@staticmethod
	def __get_partail_datas_along_x_axis(xs, ys, counts_of_points_to_plot):
		vals_dict = MatPlotUtil.get_dictionary_from_two_lists(xs, ys)
		count = 0
		nxs = []
		nys = []
		for key in sorted(vals_dict):
			if count > counts_of_points_to_plot:
				break
			for val in vals_dict[key]:
				nxs.append(key)
				nys.append(val)
			count = count + 1
		return nxs, nys

	@staticmethod
	def __get_observation_counts(dictionary):
		counts = []
		for key in sorted(dictionary):
			counts.append(len(dictionary[key]))
		return counts

	@staticmethod
	def __get_grouped_datas_along_x_axis(xs, ys, interval_len):
		interval_dic = {}
		for i in range(len(xs)):
			key = int(xs[i] / interval_len)
			if key in interval_dic:
				interval_dic[key].append(ys[i])
			else:
				interval_dic[key] = [ys[i]]

		nxs = []
		nys = []
		for key in sorted(interval_dic):
			interval_str = "{:04d}-{:04d}".format(key*interval_len, (key+1)*interval_len-1)
			for val in interval_dic[key]:
				nxs.append(interval_str)
				nys.append(val)
		return nxs, nys



