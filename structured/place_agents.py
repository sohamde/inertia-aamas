"""
Different methods to initialize and place the agents on the nodes of the created network. Node attribute 'agent' is
used to place the agents on the nodes of the network.
1. The same agent at every node
2. Randomly assigned agents at each node
3. Seed agents placed at some nodes randomly. The default agent is placed otherwise.
4. Seed agents placed at some high degree nodes. The default agent is placed otherwise.
"""

import network_agent
import globals as g
from operator import itemgetter
import random as rnd
rnd.seed()


def place_same_agent(game_phase_action):
    """ Places the same agent at every node of the network """

    for node_i in g.network.nodes():
        g.network.node[node_i]['agent'] = network_agent.NetworkAgent(game_phase_action)

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents = list(g.network.nodes())
    g.empty_nodes = []

    # updating neighbors_with_agents
    for agent_node in g.network.nodes():
        node_neighbors = g.network.neighbors(agent_node)
        g.neighbors_with_agents[agent_node] = list(node_neighbors)


def place_random_agent(game_phase_actions):
    """ Places agents of random type at each node of the network """

    for node_i in g.network.nodes():
        game_action_type = game_phase_actions[rnd.randrange(0, len(game_phase_actions))]
        g.network.node[node_i]['agent'] = network_agent.NetworkAgent(game_action_type)

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents = list(g.network.nodes())
    g.empty_nodes = []

    # updating neighbors_with_agents
    for agent_node in g.network.nodes():
        node_neighbors = g.network.neighbors(agent_node)
        g.neighbors_with_agents[agent_node] = list(node_neighbors)


def place_random_seeds(std_game_action, seed_game_action, prob):
    """ Places agents of type std_game_action, with seed agents placed with probability prob of type seed_game_action"""

    for node_i in g.network.nodes():
        seed_prob = rnd.random()
        if seed_prob <= prob:
            g.network.node[node_i]['agent'] = network_agent.NetworkAgent(seed_game_action)
        else:
            g.network.node[node_i]['agent'] = network_agent.NetworkAgent(std_game_action)

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents = list(g.network.nodes())
    g.empty_nodes = []

    # updating neighbors_with_agents
    for agent_node in g.network.nodes():
        node_neighbors = g.network.neighbors(agent_node)
        g.neighbors_with_agents[agent_node] = list(node_neighbors)


def place_high_degree_seeds(std_game_act, seed_game_act, nodes_no):
    """ Places agents of type std_game_act by default. Also places a nodes_no number of highest degree seed nodes """

    # currently a bit inefficient since the degrees for the whole network is being sorted
    network_nodes_sorted = sorted(g.network.degree_iter(), key=itemgetter(1), reverse=True)
    counter = 0
    for node_i in network_nodes_sorted:
        if counter < nodes_no:
            g.network.node[node_i[0]]['agent'] = network_agent.NetworkAgent(seed_game_act)
        else:
            g.network.node[node_i[0]]['agent'] = network_agent.NetworkAgent(std_game_act)
        counter += 1

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents = list(g.network.nodes())
    g.empty_nodes = []

    # updating neighbors_with_agents
    for agent_node in g.network.nodes():
        node_neighbors = g.network.neighbors(agent_node)
        g.neighbors_with_agents[agent_node] = list(node_neighbors)


def place_random_agent_on_node(agent_node, game_phase_actions):
    """ Places a random agent on the spot specified by agent_node """

    game_action_type = game_phase_actions[rnd.randrange(0, len(game_phase_actions))]
    g.network.node[agent_node]['agent'] = network_agent.NetworkAgent(game_action_type)

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents.append(agent_node)
    g.empty_nodes.remove(agent_node)

    # updating neighbors_with_agents
    node_neighbors = g.network.neighbors(agent_node)
    agent_neighbors = [item for item in node_neighbors if item in g.nodes_with_agents]
    g.neighbors_with_agents[agent_node] = agent_neighbors
    for node in agent_neighbors:
        g.neighbors_with_agents[node].append(agent_node)


def place_agent_on_node(agent_node, game_action):
    """ Places a specific agent of type game_action, on the spot specified by agent_node """

    g.network.node[agent_node]['agent'] = network_agent.NetworkAgent(game_action)

    # updating nodes_with_agents and empty_nodes lists
    g.nodes_with_agents.append(agent_node)
    g.empty_nodes.remove(agent_node)

    # updating neighbors_with_agents
    node_neighbors = g.network.neighbors(agent_node)
    agent_neighbors = [item for item in node_neighbors if item in g.nodes_with_agents]
    g.neighbors_with_agents[agent_node] = agent_neighbors
    for node in agent_neighbors:
        g.neighbors_with_agents[node].append(agent_node)


def delete_agent_on_node(agent_node):
    """ Deletes an specific agent on the spot specified by agent_node """

    del g.network.node[agent_node]['agent']
    g.nodes_with_agents.remove(agent_node)
    g.empty_nodes.append(agent_node)

    # updating neighbors_with_agents
    agent_neighbors = g.neighbors_with_agents[agent_node]
    for agent in agent_neighbors:
        g.neighbors_with_agents[agent].remove(agent_node)
    del g.neighbors_with_agents[agent_node]
