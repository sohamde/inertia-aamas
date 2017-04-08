# infinite well-mixed population simulations

import matplotlib.pyplot as plt

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

fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

for c in C:
    p_b = eps

    pb_list = list()
    dp_list = list()

    for t in range(T):
        dp = p_b*(1-p_b)*(c*(a+b)*p_b - (a-(1-c)*b))
        p_b += dp/dt
        pb_list.append(p_b)
        dp_list.append(dp)

    ax1.plot([i/dt for i in range(len(pb_list))], pb_list, color=colors[cnt], linewidth=2, linestyle='-')
    ax2.plot(pb_list, dp_list, color=colors[cnt], linewidth=2, linestyle='--')
    cnt += 1

title_str = 'a = '+str(a)+', b = '+str(b)
ax1.grid(b=True, which='major')
ax2.grid(b=True, which='major')
ax1.set_title(title_str)
ax2.set_title(title_str)

ax1.set_ylabel('proportion of B agents')
ax1.set_xlabel('iterations')
ax1.legend(legend_text, loc=4)
ax2.set_ylabel('rate of change of B agents')
ax2.set_xlabel('proportion of B agents')
ax2.legend(legend_text, loc=8)
plt.show()
# plt.savefig('./test.png', bbox_inches='tight', pad_inches=0)
