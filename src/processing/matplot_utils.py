from matplotlib import pyplot as plt
from matplotlib.ticker import MaxNLocator
from src.common.file_utils import FileUtil


class MatPlotUtil:
	@staticmethod
	def plot_data(x, y, point_label, x_axis_name, y_axis_name, image_directory, graph_title):
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
	def plot_all_data(x_axis_datas, y_axis_datas, x_axis_lables, y_axis_lables, graph_driectory):
		for x_index in range(len(x_axis_datas)):
			for y_index in range(len(y_axis_datas)):
				graph_title = y_axis_lables[y_index] + " vs " + x_axis_lables[x_index]
				MatPlotUtil.plot_data(x_axis_datas[x_index], y_axis_datas[y_index],
									  y_axis_lables[y_index], x_axis_lables[x_index], y_axis_lables[y_index],
									  graph_driectory, graph_title)

	@staticmethod
	def plot_jira_data(num_of_contributors, resolve_times, close_times, fix_times,
				  num_of_changed_files, num_of_changed_lines, graph_folder="../graphs"):
		x_axis_datas = [num_of_contributors, num_of_changed_lines, num_of_changed_files]
		x_axis_labels = ["Number of Contributors", "Number of Changed Lines", "Number of Changed Files"]
		y_axis_datas = [resolve_times, close_times, fix_times]
		y_axis_labels = ["Resolve Time", "Closing Time", "Bug Fix Time"]
		MatPlotUtil.plot_all_data(x_axis_datas, y_axis_datas, x_axis_labels, y_axis_labels, graph_folder)



