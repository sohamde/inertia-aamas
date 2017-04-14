import create_network as cn
import place_agents as pa
import globals as g
import game_phase as gp
import reproduction_phase as rp
import time
import random as rnd
rnd.seed()

if __name__ == "__main__":
    time_gen = 0

    # creating network and updating nodes_with_agents and empty_nodes
    cn.create_network_helper(g.network_type, g.network_model)
    pa.place_random_agent(g.game_actions)
    g.stats.step()

    # looping over generations
    while time_gen < g.num_generations:

        # switching game matrix
        if time_gen >= g.time_switch:
            g.game_matrix = g.switched_game_matrix

        gp_start = time.time()
        gp.game_phase()
        gp_time = time.time() - gp_start

        rp_start = time.time()
        rp.conformist_vs_fermi()
        rp_time = time.time() - rp_start

        end_start = time.time()
        for agent_on_node in g.nodes_with_agents:
            g.network.node[agent_on_node]['agent'].reset()

        g.stats.step()
        g.payoff_list = list()
        end_time = time.time() - end_start

        time_gen += 1

        if time_gen % 50 == 0:
            print "time: %d, gp: %f, rp: %f, end: %f" % \
                    (time_gen, gp_time, rp_time, end_time)

    g.stats.close_files()
