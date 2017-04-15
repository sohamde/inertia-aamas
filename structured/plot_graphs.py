"""
plot graphs based on the run set in file_settings
"""

import matplotlib.pyplot as plt
import csv

plt.close('all')

# list of all files to plot
folder_path = 'stats/exploration/'
prefixes = ['actions', 'mu']
file_settings = "_a0.4b0.6mu0.05c1.0grid_10_10_switch75_run0.txt"

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3']
markers = ['o', 's', '*', 'v', '^', '+', 'x', '>', '<']

titles = ['Action Proportions', 'Exploration Rates']
actions_legend = ['Norm A', 'Norm B']
legend_str = []

for i in range(len(prefixes)):
    if folder_path == 'stats/norm_change/' and prefixes[i] == 'mu':
        continue
    f_name = folder_path+prefixes[i]+file_settings
    f = open(f_name, 'rb')
    reader = csv.reader(f)
    row_num = 0
    val_num = 0
    # headers = []
    for row in reader:
        if row_num == 0:
            legend_str = row
            if prefixes[i] == 'actions':
                legend_str = actions_legend
            row_num += 1
            values = []
            continue
        for j in range(len(row)):
            if val_num < len(row):
                values.append([float(row[j])])
            else:
                values[j].append(float(row[j]))
            val_num += 1
    x_axis = range(0, len(values[0]))

    for j in range(len(markers)):
        for k in range(len(colors)):
            if j*len(colors)+k < len(values):
                plt.plot(x_axis, values[j*len(colors)+k], linestyle='-', color=colors[k], linewidth=3.0)
    plt.ylim(0., 1., 0.1)
    plt.grid('on')
    plt.ylabel('Proportions').set_size(16)
    plt.legend(legend_str)
    plt.xlabel('Generations').set_size(16)
    plt.title(titles[i])
    plt.show()
    f.close()
