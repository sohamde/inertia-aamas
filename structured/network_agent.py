"""
Agent class for specifying the nodes of the network

Agent types:

Game Phase
A: plays action A
B: plays action B

@author: Soham De
@email: sohamde@cs.umd.edu
@date: Nov 5, 2014

"""

import random as rnd
rnd.seed()


class NetworkAgent:
	""" NetworkAgent class defines the agents on the nodes of the network """

	def __init__(self, game_phase_action):
		""" Creates class objects of the game phase types and punishment phase types """

		if game_phase_action == "A":
			self.game_action_type = NormA()
		elif game_phase_action == "B":
			self.game_action_type = NormB()

		self.games_played = list()
		self.agents_played = list()
		self.payoff = 0.0

	def move(self, game, agent_num):
		""" Returns the game phase move; return 0 for A, 1 for B"""

		opponent = self.get_opponent(game)
		return self.game_action_type.move(game, opponent, agent_num)

	def get_opponent(self, game):
		""" Returns the opponent of the agent in the current game """
		if game.player_1 == self:
			opponent = game.player_2
		else:
			opponent = game.player_1
		return opponent

	def total_payoff(self):
		""" Returns total payoff received from all games played """
		return sum(game.payoffs()[self] for game in self.games_played)

	def reset(self):
		""" Resents history to empty """

		self.games_played = list()
		self.agents_played = list()
		self.payoff = 0.0

	def record(self, game):
		""" Records the game played to history """

		self.games_played.append(game)
		opponent = self.get_opponent(game)
		self.agents_played.append(opponent)


class NormA:
	""" NormA class defines agents who always play Norm A """

	def __init__(self):
		self.game_action = "A"

	def move(self, game, opponent, agent_num):
		return 0


class NormB:
	""" NormB class defines agents who always play Norm B """

	def __init__(self):
		self.game_action = "B"

	def move(self, game, opponent, agent_num):
		return 1
