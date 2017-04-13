"""
Using replicator dynamics on an infinite well-mixed population
Examining norm change from A to B under differing coordination needs for a population with majority initially playing A
"""

import matplotlib.pyplot as plt

# set the no of iterations per time step dt, and total no of iterations T for the simulation
dt = 20000.0
T = 100*int(dt)

# set the weighting factor that controls the need for coordination
# 1 means high need for coordination with others, 0 means no need for coordination
C = [0.05, 0.3]    # C denotes the set of all weighting factors to compare against

# starting proportion of B agents in the population
eps = 0.05

# parameters for game matrix
a = 0.3
b = 0.7

# setting the legend for the output plots
legend_text = []
for c in C:
    legend_text.append('c = '+str(c))

# creating plots
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# setting colors for plots and counter to keep track of colors used
colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3']
cnt = 0

# looping over different runs for different c values
for c in C:
    # setting proportion of B agents
    p_b = eps

    # defining lists to keep track of proportion of B agents (pb_list), and change in that proportion, in each time step
    pb_list = list()
    dp_list = list()

    # running replicator dynamics for T iterations
    for t in range(T):
        dp = p_b*(1-p_b)*(c*(a+b)*p_b - (a-(1-c)*b))    # change in proportion of B agents using replicator dynamics
        p_b += dp/dt                                    # updating proportion of B agents

        # updating lists
        pb_list.append(p_b)
        dp_list.append(dp)

    # plotting proportion and change in proportion for B agents using stored lists
    ax1.plot([i/dt for i in range(len(pb_list))], pb_list, color=colors[cnt], linewidth=2, linestyle='-')
    ax2.plot(pb_list, dp_list, color=colors[cnt], linewidth=2, linestyle='-')
    cnt += 1

# settings for plots
title_str = 'a = '+str(a)+', b = '+str(b)
ax1.set_title(title_str)
ax2.set_title(title_str)

ax1.grid(b=True, which='major')
ax2.grid(b=True, which='major')

ax1.set_ylabel('proportion of B agents')
ax1.set_xlabel('iterations')
ax1.legend(legend_text, loc=4)
ax2.set_ylabel('rate of change of B agents')
ax2.set_xlabel('proportion of B agents')
ax2.legend(legend_text, loc=8)
plt.show()
