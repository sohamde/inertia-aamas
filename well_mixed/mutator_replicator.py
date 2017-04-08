# infinite well-mixed population simulations

import matplotlib.pyplot as plt
import sys
from decimal import Decimal
from pylab import *

im_folder = '/Users/soham/Dropbox-personal/Dropbox/Social_Norms/Norm_Change/aamas/images/figure_3/'

dt = 20000.0
# T = 100*int(dt)
T = 100*int(dt)

C = [0.05, 0.3]
# mu = [0.0, 0.025, 0.05, 0.075, 0.1]
mu = [0.0, 0.03, 0.06, 0.1]
legend_str = []

a_c = 0.4
b_c = 0.6

b_f = (a_c + b_c) / 2
a_f = b_f - (b_c - a_c)

if C[0] > (b_c - a_c)/b_c or C[1] > (b_c - a_c)/b_c:
	print "no norm change"
	sys.exit(0)

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3', '0.1', '0.5', '0.7', '0.9']
linestyles = ['-', '--']
cnt2 = 0

for c in C:
	M = [[c*a_c + (1-c)*a_f, (1-c)*a_f], [(1-c)*b_f, c*b_c + (1-c)*b_f]]
	cnt = 0
	ls = linestyles[cnt2]
	cnt2 += 1

	for m in mu:
		legend_str.append('c'+str(c)+', mu'+str(m))
		p_b = 0
		if m == 0:
			p_b = 0.05
		pb_list = list()
		dp_list = list()

		for t in range(T):
			dp_1 = p_b*(1-p_b)*(c*(a_c+b_c)*p_b-(a_c-(1-c)*b_c))
			dp_2 = m*(p_b*(1-p_b)*(a_c-b_c) + c*(((1-p_b)**2)*a_c-(p_b**2)*b_c) + (1-c)*(((1-p_b)**2)*a_f-(p_b**2)*b_f))
			dp = dp_1 + dp_2
			p_b += dp/dt
			pb_list.append(p_b)
			dp_list.append(dp)

		figure(0)
		plt.plot([i/dt for i in range(len(pb_list))], pb_list, color=colors[cnt], linewidth=3, linestyle=ls)
		figure(1)
		plt.plot(pb_list, dp_list, color=colors[cnt], linewidth=3, linestyle=ls)
		cnt += 1
		print 'c = ', c, 'mu = ', m

for i in range(2):
	figure(i)
	plt.minorticks_on()
	plt.rcParams.update({'font.size': 20})
	title_str = 'a='+str(a_c)+', b='+str(b_c)
	plt.grid(b=True, which='major')
	plt.grid(b=True, which='minor')
	plt.title(title_str)
figure(0)
plt.ylabel('proportion of B agents')
plt.xlabel('iterations')
# plt.legend(legend_str, loc=4)
plt.legend(mu, loc=4)
figure(1)
plt.ylabel('rate of change of B agents')
plt.xlabel('proportion of B agents')
# plt.legend(legend_str, loc=8)
plt.legend(mu, loc=8)

# plt.show()
figure(0)
im_name = 'inf_a'+str(int(round(Decimal(a_c*100))))+'b'+str(int(round(Decimal(b_c*100))))+'_inertia.png'
plt.savefig(str(im_folder+im_name), bbox_inches='tight', pad_inches=0)
figure(1)
im_name = 'inf_a'+str(int(round(Decimal(a_c*100))))+'b'+str(int(round(Decimal(b_c*100))))+'_inertia_rate.png'
plt.savefig(str(im_folder+im_name), bbox_inches='tight', pad_inches=0)
