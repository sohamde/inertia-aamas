"""
Methods to create different network structures

Each node is an agent class object
Each edge can be associated with a class object containing history of interaction

Current methods:
2D grid of size MxN
Watts-Strogatz network model with average degree D

@author: Soham De
@email: sohamde@cs.umd.edu
@date: Nov 5, 2014

"""

import networkx as nx
import globals as g


def grid_network(rows, cols):
	"""creates a 2D grid network with arg1 rows and arg2 columns"""
	g.network = nx.grid_2d_graph(rows, cols, periodic=True)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def watts_strogatz_network(nodes, degree, rewiring_probability):
	"""creates a network using the Watts-Strogatz model"""
	g.network = nx.watts_strogatz_graph(nodes, degree, rewiring_probability)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def erdos_renyi(nodes, edge_probability):
	"""creates a network using the Erdos-Renyi model """
	g.network = nx.erdos_renyi_graph(nodes, edge_probability)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def connected_caveman(no_cliques, size_cliques):
	"""creates a network using the Connected Caveman model """
	g.network = nx.connected_caveman_graph(no_cliques, size_cliques)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def barabasi_albert(nodes, edges):
	"""creates a network using the Barabasi-Albert model """
	g.network = nx.barabasi_albert_graph(nodes, edges)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def random_regular(nodes, degree):
	"""creates a random regular graph"""
	g.network = nx.random_regular_graph(degree, nodes)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def hierarchical_poisson_clusters(nodes, no_clusters, high_p, low_p):
	"""creates a hierarchical Poisson random graph"""
	G = nx.Graph()
	nodes_per_cluster = nodes/no_clusters
	for i in range(no_clusters):
		G1 = nx.gnp_random_graph(nodes_per_cluster, high_p)
		mapping = dict(zip(G1.nodes(), range(i*nodes_per_cluster, (i+1)*nodes_per_cluster)))
		G1 = nx.relabel_nodes(G1, mapping)
		G = nx.compose(G, G1)
	G1 = nx.gnp_random_graph(nodes, low_p)
	g.network = nx.compose(G, G1)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def star_graph(nodes):
	"""creates a star graph with 1 central node and (nodes-1) terminal nodes"""
	g.network = nx.star_graph(nodes-1)
	g.empty_nodes = g.network.nodes()
	g.nodes_with_agents = []
	g.neighbors_with_agents = {}


def create_network_helper(network_type, model_params):
	"""calls the appropriate create network model based on network_type"""
	if network_type == "grid":
		grid_network(model_params[0], model_params[1])
	elif network_type == "watts":
		watts_strogatz_network(model_params[0], model_params[1], model_params[2])
	elif network_type == "clusters":
		hierarchical_poisson_clusters(model_params[0], model_params[1], model_params[2], model_params[3])
	elif network_type == "random":
		erdos_renyi(model_params[0], model_params[1])
	elif network_type == "caveman":
		connected_caveman(model_params[0], model_params[1])
	elif network_type == "barabasi":
		barabasi_albert(model_params[0], model_params[1])
	elif network_type == "star":
		star_graph(model_params[0])
	elif network_type == "regular":
		random_regular(model_params[0], model_params[1])
