# infinite well-mixed population simulations

from pylab import *
import seaborn as sns
sns.set_context("paper", font_scale=1.0, rc={"lines.linewidth": 2.5})
sns.set_style("darkgrid", {"axes.facecolor": ".9", 'font.sans-serif': u'Liberation Sans'})
# dt = 20000.0
# T = 100*int(dt)
dt = 2000.0
T = 25*int(dt)

C = [0.05, 0.3]
legend_text = ['c = '+str(C[0]), 'c = '+str(C[1])]
eps = 0.05

a = 0.3
b = 0.7

colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3']
cnt = 0

for c in C:
    p_b = eps

    pb_list = list()
    dp_list = list()

    for t in range(T):
        dp = p_b*(1-p_b)*(c*(a+b)*p_b - (a-(1-c)*b))
        p_b += dp/dt
        pb_list.append(p_b)
        dp_list.append(dp)

    figure(0)
    # plt.plot([i/dt for i in range(len(pb_list))], pb_list, color=colors[cnt], linewidth=2, linestyle='-')
    plt.plot([i/dt for i in range(len(pb_list))], pb_list, linestyle='-')
    figure(1)
    # plt.plot(pb_list, dp_list, color=colors[cnt], linewidth=2, linestyle='--')
    plt.plot(pb_list, dp_list, linestyle='--')
    cnt += 1

for i in range(2):
    figure(i)
    title_str = 'a = '+str(a)+', b = '+str(b)
    plt.grid(b=True, which='major')
    # plt.grid(b=True, which='minor')
    plt.title(title_str)

figure(0)
plt.ylabel('proportion of B agents')
plt.xlabel('iterations')
plt.legend(legend_text, loc=4)
figure(1)
plt.ylabel('rate of change of B agents')
plt.xlabel('proportion of B agents')
plt.legend(legend_text, loc=8)
plt.show()
# plt.savefig('./test.png', bbox_inches='tight', pad_inches=0)
