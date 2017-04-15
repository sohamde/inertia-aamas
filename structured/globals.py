"""
Contains all the global variables in the games on network framework. File needs to be imported in other functions.
"""

import networkx as nx
import stats_files as st
import sys
import os

# set path to folder where output files will be saved; cluster = 1 if running on DeepThought2 cluster, 0 otherwise
cluster_dir = "/lustre/sohamde/Inertia-AAMAS"
if os.path.isdir(cluster_dir):
    cluster = 1
    folder_path = cluster_dir+"/stats"
else:
    cluster = 0
    folder_path = "./stats"

if not os.path.exists(folder_path):
    os.makedirs(folder_path)
if not os.path.exists(folder_path + "/norm_change"):
    os.makedirs(folder_path + "/norm_change")
if not os.path.exists(folder_path + "/exploration"):
    os.makedirs(folder_path + "/exploration")

# game and punishment phase actions
game_actions = ['A', 'B']

# game matrix payoffs
a = float(sys.argv[1])
b = float(sys.argv[2])

# need for coordination
c = float(sys.argv[6])
if c < 0 or c > 1:
    sys.exit("the condition 0 <= c <= 1 is violated")

# two player game matrix
game_matrix_1 = [[(a, a), ((1-c)*a, (1-c)*b)], [((1-c)*b, (1-c)*a), (b, b)]]
game_matrix_2 = [[(b, b), ((1-c)*b, (1-c)*a)], [((1-c)*a, (1-c)*b), (a, a)]]
game_matrix = game_matrix_1

# initializing the network structure
network = nx.Graph()
network_type = str(sys.argv[3])              # 'watts' for watts strogatz model, 'grid' for grid network
network_parameters_str = str(sys.argv[4])
network_parameters_list = network_parameters_str.split(",")
network_model = []
if network_type == 'grid':
    network_model = [int(i) for i in network_parameters_list]
elif network_type == 'watts':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(int(network_parameters_list[1]))
    network_model.append(float(network_parameters_list[2]))
elif network_type == 'clusters':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(int(network_parameters_list[1]))
    network_model.append(float(network_parameters_list[2]))
    network_model.append(float(network_parameters_list[3]))
elif network_type == 'random':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(float(network_parameters_list[1]))
elif network_type == 'caveman':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(int(network_parameters_list[1]))
elif network_type == 'barabasi':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(int(network_parameters_list[1]))
elif network_type == 'star':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
elif network_type == 'regular':
    network_model = list()
    network_model.append(int(network_parameters_list[0]))
    network_model.append(int(network_parameters_list[1]))

# basic game settings
run = int(sys.argv[5])      # run number: useful when running the same configuration multiple times
games_per_round = 0         # number of games each agent plays in a round; set to 0 for pairing all neighbors
mu_rate = 0.05    # probability of an agent mutating to a random strategy
if sys.argv[0] == 'main_explore.py':
    mutation_rate_types = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
    mutation_rates = {}  # dictionary with nodes as keys and agent neighbors as values
    base_mu_rate = mu_rate

# number of generations, and generation at which to switch the game matrix
if cluster == 1:
    num_generations = 6000
    time_switch = 2500  # make equal to num_generations if no switch is desired
else:
    num_generations = 2000
    time_switch = 1000
if sys.argv[0] == 'main_explore.py':
    time_switch = 75

# lists and dicts for keeping tracking of the games
nodes_with_agents = []      # nodes with agents on them
empty_nodes = []            # nodes without agents on them
neighbors_with_agents = {}  # dictionary with nodes as keys and agent neighbors as values
normA_percentage = 0        # percentage of agents playing norm A
payoff_list = list()        # list of payoffs received by the agents

# file name also includes the run number, which is passed as a separate command line argument
run_ID = "a" + str(a) + "b" + str(b) + "mu" + str(mu_rate) + "c" + str(c)
if network_type == "grid":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1])
elif network_type == "watts":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1]) + "_" + str(network_model[2])
elif network_type == "clusters":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1]) + "_" + str(network_model[2])
    run_ID += "_" + str(network_model[3])
elif network_type == "random":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1])
elif network_type == "caveman":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1])
elif network_type == "barabasi":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1])
elif network_type == "star":
    run_ID += network_type + "_" + str(network_model[0])
elif network_type == "regular":
    run_ID += network_type + "_" + str(network_model[0]) + "_" + str(network_model[1])
if time_switch < num_generations:
    run_ID += "_switch" + str(time_switch)
run_ID += "_run" + str(run)

# initializing stats class
stats = st.Stats(game_actions, run_ID)
