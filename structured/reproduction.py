"""
contains functions that define the reproduction rules used in the evolutionary game
"""

import globals as g
import place_agents as pa
import networkx as nx
import random as rnd
from math import exp
rnd.seed()


def fermi():
    # calculate highest and lowest payoff
    min_d = min(nx.degree(g.network).values())
    max_d = max(nx.degree(g.network).values())
    if g.games_per_round == 0:
        min_degree = min_d
        max_degree = max_d
    else:
        min_degree = min(min_d, g.games_per_round)
        max_degree = max(max_d, g.games_per_round)
    low_payoff = float((1-g.c)*min(g.a, g.b)*min_degree)
    high_payoff = float(max(g.a, g.b)*max_degree)
    range_payoff = high_payoff - low_payoff

    # randomly permuting the agents
    rnd.shuffle(g.nodes_with_agents)

    # nodes with agents on them
    agent_nodes = list(g.nodes_with_agents)

    # for each agent in the network
    for agent_node in agent_nodes:
        # get neighbors
        node_neighbors = g.network.neighbors(agent_node)

        # choose teacher
        teacher_loc = rnd.choice(node_neighbors)

        # normalizing payoffs
        teacher_payoff = (g.network.node[teacher_loc]['agent'].payoff - low_payoff) / range_payoff
        agent_payoff = (g.network.node[agent_node]['agent'].payoff - low_payoff) / range_payoff
        payoff_difference = teacher_payoff - agent_payoff

        if rnd.random() < 1.0 / (1.0 + exp(-5.0 * payoff_difference)):
            # getting game action and punishment action of teacher
            agent_game_action = g.network.node[teacher_loc]['agent'].game_action_type.game_action

            # copying teacher's strategy with mutation
            if rnd.random() < g.mu_rate:
                pa.delete_agent_on_node(agent_node)
                pa.place_random_agent_on_node(agent_node, g.game_actions)
            else:
                pa.delete_agent_on_node(agent_node)
                pa.place_agent_on_node(agent_node, agent_game_action)


def fermi_explore():
    # calculate highest and lowest payoff
    min_d = min(nx.degree(g.network).values())
    max_d = max(nx.degree(g.network).values())
    if g.games_per_round == 0:
        min_degree = min_d
        max_degree = max_d
    else:
        min_degree = min(min_d, g.games_per_round)
        max_degree = max(max_d, g.games_per_round)
    low_payoff = float((1-g.c)*min(g.a, g.b)*min_degree)
    high_payoff = float(max(g.a, g.b)*max_degree)
    range_payoff = high_payoff - low_payoff

    # randomly permuting the agents
    rnd.shuffle(g.nodes_with_agents)

    # nodes with agents on them
    agent_nodes = list(g.nodes_with_agents)

    # for each agent in the network
    for agent_node in agent_nodes:
        # get neighbors
        node_neighbors = g.network.neighbors(agent_node)

        # choose teacher
        teacher_loc = rnd.choice(node_neighbors)

        # normalizing payoffs
        teacher_payoff = (g.network.node[teacher_loc]['agent'].payoff - low_payoff) / range_payoff
        agent_payoff = (g.network.node[agent_node]['agent'].payoff - low_payoff) / range_payoff
        payoff_difference = teacher_payoff - agent_payoff

        if rnd.random() < g.mutation_rates[agent_node]:
            pa.delete_agent_on_node(agent_node)
            pa.place_random_agent_on_node(agent_node, g.game_actions)

        if rnd.random() < g.base_mu_rate:
            g.mutation_rates[agent_node] = rnd.choice(g.mutation_rate_types)

        if rnd.random() < 1.0 / (1.0 + exp(-5.0 * payoff_difference)):
            # getting game action and punishment action of teacher
            agent_game_action = g.network.node[teacher_loc]['agent'].game_action_type.game_action

            # copying teacher's strategy with mutation
            pa.delete_agent_on_node(agent_node)
            pa.place_agent_on_node(agent_node, agent_game_action)
            g.mutation_rates[agent_node] = g.mutation_rates[teacher_loc]
