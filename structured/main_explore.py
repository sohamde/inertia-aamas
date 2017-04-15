"""
main file for running experiments to study the evolution of exploration rates
"""

import create_network as cn
import place_agents as pa
import globals as g
import game_phase as gp
import reproduction as rp
import time
import random as rnd
rnd.seed()

if __name__ == "__main__":
    time_gen = 0

    # creating network and updating nodes_with_agents and empty_nodes
    cn.create_network_helper(g.network_type, g.network_model)
    pa.place_random_agent(g.game_actions)
    for node_i in g.network.nodes():
        g.mutation_rates[node_i] = rnd.choice(g.mutation_rate_types)
    g.stats.step()

    # looping over generations
    while time_gen < g.num_generations:

        # switching game matrix
        if (time_gen/g.time_switch) % 2 == 0:
            g.game_matrix = g.game_matrix_1
        else:
            g.game_matrix = g.game_matrix_2

        # game phase
        gp_start = time.time()
        gp.game_phase()
        gp_time = time.time() - gp_start

        # reproduction phase
        rp_start = time.time()
        rp.fermi_explore()
        rp_time = time.time() - rp_start

        # reset agents
        end_start = time.time()
        for agent_on_node in g.nodes_with_agents:
            g.network.node[agent_on_node]['agent'].reset()

        # save statistics
        g.stats.step()
        g.payoff_list = list()
        end_time = time.time() - end_start

        time_gen += 1

        if time_gen % 50 == 0:
            print "time: %d" % time_gen

    g.stats.close_files()
