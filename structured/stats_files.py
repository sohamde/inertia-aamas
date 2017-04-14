"""
Keeps track of population statistics
Author: Soham De
Email: sohamde at cs umd edu
"""

import globals as g
from collections import defaultdict


class Stats:

    def __init__(self, game_actions, run_ID="x"):
        """ Initializing the log files with header information """

        self.game_actions = game_actions

        if g.cluster == 1:
            self.game_actions_file = open("/lustre/sohamde/InertiaNormChange/stats/allProps_"+str(run_ID)+".txt", 'wb')
        elif g.cluster == 0:
            self.game_actions_file = open("./stats/allProps_"+str(run_ID)+".txt", 'wb')
        for t in game_actions:
            if t == game_actions[-1]:
                self.game_actions_file.write(t+"\n")
            else:
                self.game_actions_file.write(t+",")

        # if g.cluster == 1:
        # 	self.stats_file = open("/lustre/sohamde/NetworkGames/stats/stats_"+str(run_ID)+".txt", 'wb')
        # elif g.cluster == 0:
        # 	self.stats_file = open("./stats/stats_"+str(run_ID)+".txt", 'wb')
        # self.stats_file.write("total_population_payoff,cooperation_percentage\n")

    def step(self):
        """ Records everything for this time step. """

        game_action_proportions = self.count_population_proportions()

        # proportions of strategy types
        for t in self.game_actions:
            if t == self.game_actions[-1]:
                self.game_actions_file.write(str(game_action_proportions[t])+"\n")
            else:
                self.game_actions_file.write(str(game_action_proportions[t])+",")

        # self.stats_file.write(str(sum(g.payoff_list))+","+str(g.normA_percentage)+"\n")

    def count_population_proportions(self):

        game_action_proportions = defaultdict(float)

        for node in g.nodes_with_agents:
            a = g.network.node[node]['agent']
            for t in self.game_actions:
                if a.game_action_type.game_action == t:
                    game_action_proportions[t] += 1

        for t in self.game_actions:
            if len(g.nodes_with_agents) > 0:
                game_action_proportions[t] = float(game_action_proportions[t])/len(g.nodes_with_agents)
            else:
                game_action_proportions[t] = 0

        return game_action_proportions

    def close_files(self):

        self.game_actions_file.close()
        # self.stats_file.close()
