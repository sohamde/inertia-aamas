"""
Using replicator-mutator dynamics on an infinite well-mixed population
Examining norm change from A to B under differing coordination needs and differing exploration rates
"""

import matplotlib.pyplot as plt

# set the no of iterations per time step dt, and total no of iterations T for the simulation
dt = 20000.0
T = 100*int(dt)

# set the weighting factor that controls the need for coordination
# 1 means high need for coordination with others, 0 means no need for coordination
C = [0.05, 0.3]     # C denotes the set of all weighting factors to compare against

# set of exploration rates
mu = [0.0, 0.03, 0.06, 0.1]

# parameters for game matrix
a = 0.4
b = 0.6

# creating plots
fig1, ax1 = plt.subplots()
fig2, ax2 = plt.subplots()

# setting colors and line styles for plots and counter to keep track of colors used
clr = ['b', 'g', 'r', 'c', 'm', 'y', 'k', '0.3', '0.1', '0.5', '0.7', '0.9']
line_styles = ['-', '--', '-.', ':']
cnt2 = 0

# looping over different runs for different c and mu values
for c in C:
    # setting parameters for plots
    cnt = 0
    ls = line_styles[cnt2]
    cnt2 += 1

    # looping over mu values
    for m in mu:
        print 'running c =', c, 'mu =', m

        # if exploration rate is 0, the proportion of B agents starts from 0.05 as in the replicator dynamic case
        p_b = 0
        if m == 0:
            p_b = 0.05

        # defining lists to keep track of proportion of B agents, and change in that proportion, in each time step
        pb_list = list()
        dp_list = list()

        # running replicator-mutator dynamics for T iterations
        for t in range(T):
            # change in proportion of B agents using replicator-mutator dynamics
            dp = p_b*(1-p_b)*(c*(a+b)*p_b-(a-(1-c)*b)) + m*(p_b*(1-p_b)*(1-c)*(a-b) + (((1-p_b)**2)*a-(p_b**2)*b))
            p_b += dp/dt            # updating proportion of B agents

            # updating lists
            pb_list.append(p_b)
            dp_list.append(dp)

        # plotting proportion and change in proportion for B agents using stored lists
        ax1.plot([i/dt for i in range(len(pb_list))][::500], pb_list[::500], color=clr[cnt], linewidth=2, linestyle=ls)
        ax2.plot(pb_list[::500], dp_list[::500], color=clr[cnt], linewidth=2, linestyle=ls)
        cnt += 1

# settings for plots
title_str = 'a = '+str(a)+', b = '+str(b)
ax1.set_title(title_str)
ax2.set_title(title_str)

ax1.grid(b=True, which='major')
ax2.grid(b=True, which='major')

ax1.set_ylabel('proportion of B agents')
ax1.set_xlabel('iterations')
ax1.legend(mu, loc=4)
ax2.set_ylabel('rate of change of B agents')
ax2.set_xlabel('proportion of B agents')
ax2.legend(mu, loc=8)
plt.show()
