"""
plot graphs based on the files in settings_list
"""

import matplotlib.pyplot as plt
import csv

plt.close('all')

# list of all files to plot
settings_list = ["_a0.4b0.6mu0.05c1.0grid_10_10_switch1000_run0.txt",
                 "_a0.4b0.6mu0.05c0.75grid_10_10_switch1000_run0.txt",
                 "_a0.4b0.6mu0.05c0.5grid_10_10_switch1000_run0.txt"]
file_path = 'stats/'

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3']
markers = ['o', 's', '*', 'v', '^', '+', 'x', '>', '<']
prefixes = ['actions', 'mu']
titles = ['Action Proportions', 'Exploration Rates']
headers = ['Norm A', 'Norm B']

count = 0

for settings in settings_list:
    plt.subplot(len(settings_list), 1, count+1)
    for i in range(len(prefixes)):
        f_name = file_path+prefixes[i]+settings
        f = open(f_name, 'rb')
        reader = csv.reader(f)
        row_num = 0
        val_num = 0
        # headers = []
        for row in reader:
            if row_num == 0:
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
        if count == len(settings_list)/2:
            plt.ylabel('Proportions').set_size(16)
        if count == 0:
            plt.legend(headers, loc='upper center', bbox_to_anchor=(0.5, 1.35), frameon=False, ncol=5)
        f.close()

    count += 1

plt.xlabel('Generations').set_size(16)
plt.show()
