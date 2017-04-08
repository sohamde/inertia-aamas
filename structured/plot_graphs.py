import matplotlib.pyplot as plt
import csv
import sys

plt.close('all')

# settings = '_coord_a1.0b1.4mu0.05weight0.75conf0.8grid_30_30_switch2500_avg.txt'
# settings = '_coord_a1.0b1.4mu0.05weight1.0conf0.0watts_1000_4_0.1_switch2500_avg.txt'
# settings = '_coord_a1.0b1.005mu0.05weight0.5conf0.0watts_1000_14_0.1_switch2500_avg.txt'
# settings = '_coord_a0.45b0.55mu0.05weight1.0conf0.0barabasi_100_2_switch1000_run0.txt'
# settings = '_coord_a0.15b0.85mu0.05weight1.0conf0.0star_100_switch1000_run0.txt'
# settings = '_coord_a0.3b0.7mu0.05weight1.0conf0.0watts_100_4_0.1_switch1000_run0.txt'
# settings = '_coord_a0.3b0.7mu0.05weight0.5conf0.0watts_100_14_0.1_switch1000_run0.txt'

# settings_list = ['_coord_a1.0b2.0mu0.05weight0.75conf0.8watts_1000_14_0.1_switch2500_avg.txt',
# 				 # '_coord_a1.0b1.4mu0.05weight0.75conf0.4grid_50_50_switch2500_avg.txt',
# 				 '_coord_a1.0b2.0mu0.05weight0.75conf0.0watts_1000_4_0.1_switch2500_avg.txt']
# im_name = 'cm_b14_w075.png'

settings_list = ['_coord_a1.0b1.15mu0.05weight1.0conf0.0grid_50_50_switch2500_avg.txt',
				 '_coord_a1.0b1.15mu0.05weight0.75conf0.0grid_50_50_switch2500_avg.txt',
				 '_coord_a1.0b1.15mu0.05weight0.5conf0.0grid_50_50_switch2500_avg.txt']
im_name = 'gm_b115_c0.png'

# tests
# settings_list = ['_coord_a1.0b5.0mu0.05weight1.0conf0.0watts_100_50_0.1_switch2500_avg.txt',
#                  '_coord_a1.0b5.0mu0.05weight0.75conf0.8watts_100_50_0.1_switch2500_avg.txt',
#                  '_coord_a1.0b5.0mu0.05weight1.0conf0.0random_100_1.0_switch2500_avg.txt',
#                  '_coord_a1.0b5.0mu0.05weight0.75conf0.8random_100_1.0_switch2500_avg.txt']
#                  # '_coord_a0.3b0.7mu0.05weight1.0conf0.0watts_100_14_0.1_switch1000_run0.txt']

# f_img, ax_arr = plt.subplots(1, len(settings_list), sharey=True)

# settings_list = ['_coord_a1.0b3.0mu0.05weight0.25conf0.0regular_100_10_switch2500_avg.txt']

# file_path = 'stats/moran_runs1/'
file_path = 'stats/final_runs/'
# plt.figure(figsize=(6, 3))

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3']
markers = ['o', 's', '*', 'v', '^', '+', 'x', '>', '<']
prefixes = ['allProps']
titles = ['Strategy Proportions']
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
					plt.plot(x_axis, values[j*len(colors)+k], linestyle='-', color=colors[k], linewidth=3.0)  # label=headers[j*len(colors)+k]
		plt.ylim(0., 1., 0.1)
		plt.grid('on')
		if count == len(settings_list)/2:
			plt.ylabel('Proportions').set_size(16)
		if count == 0:
			plt.legend(headers, loc='upper center', bbox_to_anchor=(0.5, 1.35), frameon=False, ncol=5)   # fancybox=False, shadow=False, )
		f.close()

	count += 1

plt.xlabel('Generations').set_size(16)

if sys.argv[1] == 'show':
	plt.show()
elif sys.argv[1] == 'save':
	im_folder = '/Users/soham/Dropbox-personal/Dropbox/Social_Norms/Inertia&SocialLearning/Paper_Draft/images/'
	plt.savefig(str(im_folder+im_name), bbox_inches='tight', pad_inches=0.1)
