from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
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
		MatPlotUtil.pointplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory+"/PointPlot", graph_title)
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
	def boxplot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
		# # plt.style.use('ggplot')
		# fig, ax = plt.subplots(figsize=(30, 25))

		fig, ax = plt.subplots()
		dictionary = MatPlotUtil.get_dictionary_from_two_lists(x, y)
		data = MatPlotUtil.get_dict_vals_as_2d_list(dictionary)
		labels = sorted(dictionary)

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
		return values_dict

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

