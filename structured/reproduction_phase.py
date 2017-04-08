import globals as g
import place_agents as pa
import networkx as nx
import random as rnd
from math import exp
rnd.seed()


def conformist_vs_fermi():
	"""with probability g.conf_fermi_prob, use the action played by majority of the neighbors. else use fermi rule"""

	# calculate highest and lowest payoff
	min_d = min(nx.degree(g.network).values())
	max_d = max(nx.degree(g.network).values())
	if g.games_per_round == 0:
		min_degree = min_d
		max_degree = max_d
	else:
		min_degree = min(min_d, g.games_per_round)
		max_degree = max(max_d, g.games_per_round)
	low_payoff = float((1-g.w)*g.d*min_degree)
	high_payoff = float(((1-g.w)*g.d + g.w*g.b)*max_degree)
	range_payoff = high_payoff - low_payoff

	# randomly permuting the agents
	rnd.shuffle(g.nodes_with_agents)

	# nodes with agents on them
	agent_nodes = list(g.nodes_with_agents)

	# for each agent in the network
	for agent_node in agent_nodes:

		# get neighbors
		node_neighbors = g.network.neighbors(agent_node)

		# use conformism or fermi
		p = rnd.random()

		if p < g.conf_fermi_prob:
			# choose majority
			num_A = 0
			num_B = 0

			for adjacent_node in node_neighbors:
				neighbor_game_action = g.network.node[adjacent_node]['agent'].game_action_type.game_action
				if neighbor_game_action == 'A':
					num_A += 1
				elif neighbor_game_action == 'B':
					num_B += 1

			if num_A > num_B:
				agent_game_action = 'A'
			elif num_B > num_A:
				agent_game_action = 'B'
			else:
				# if no clear majority, do not change strategy
				agent_game_action = g.network.node[agent_node]['agent'].game_action_type.game_action

			if rnd.random() < g.mu_rate:
				pa.delete_agent_on_node(agent_node)
				pa.place_random_agent_on_node(agent_node, g.game_actions)
			else:
				pa.delete_agent_on_node(agent_node)
				pa.place_agent_on_node(agent_node, agent_game_action)

		else:   # fermi rule
			# choose teacher
			teacher_loc = rnd.choice(node_neighbors)

			# normalizing payoffs
			teacher_payoff = (g.network.node[teacher_loc]['agent'].payoff - low_payoff)/range_payoff
			agent_payoff = (g.network.node[agent_node]['agent'].payoff - low_payoff)/range_payoff
			payoff_difference = teacher_payoff - agent_payoff

			if rnd.random() < 1.0/(1.0 + exp(-5.0*payoff_difference)):

				# getting game action and punishment action of teacher
				agent_game_action = g.network.node[teacher_loc]['agent'].game_action_type.game_action

				# copying teacher's strategy with mutation
				if rnd.random() < g.mu_rate:
					pa.delete_agent_on_node(agent_node)
					pa.place_random_agent_on_node(agent_node, g.game_actions)
				else:
					pa.delete_agent_on_node(agent_node)
					pa.place_agent_on_node(agent_node, agent_game_action)


def moran():
	""" random agent dies off; neighbors reproduce into that spot with probability proportional to fitness """

	# randomly permuting the agents
	rnd.shuffle(g.nodes_with_agents)

	# pick a random agent that dies off, and get neighbors
	agent_node = rnd.choice(g.nodes_with_agents)
	node_neighbors = g.network.neighbors(agent_node)

	# iterate over agent neighbors to calculate total payoff
	neighbor_payoff_sum = 0
	neighbor_A_payoff = 0
	for adjacent_node in node_neighbors:
		neighbor_payoff_sum += g.network.node[adjacent_node]['agent'].payoff
		if g.network.node[adjacent_node]['agent'].game_action_type.game_action == 'A':
			neighbor_A_payoff += g.network.node[adjacent_node]['agent'].payoff

	# if every neighbor has zero payoff, replace by random agent
	if neighbor_payoff_sum == 0:
		pa.delete_agent_on_node(agent_node)
		pa.place_random_agent_on_node(agent_node, g.game_actions)
		return

	# selecting agent to reproduce into agent_node
	p = rnd.random()
	if p <= float(neighbor_A_payoff)/neighbor_payoff_sum:
		agent_game_action = 'A'
	else:
		agent_game_action = 'B'

	# copying teacher's strategy with mutation
	if rnd.random() < g.mu_rate:
		pa.delete_agent_on_node(agent_node)
		pa.place_random_agent_on_node(agent_node, g.game_actions)
	else:
		pa.delete_agent_on_node(agent_node)
		pa.place_agent_on_node(agent_node, agent_game_action)
