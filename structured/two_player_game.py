"""
Runs a two player game between two agents

"""


class TwoPlayerGame:

    def __init__(self, p1, p2, matrix, gp_actions, agent_node, opponent):
        """ Initializes the two player game; p1: Row player; p2: Column player """

        self.player_1 = p1
        self.player_2 = p2
        self.game_matrix = matrix
        self.game_actions = gp_actions
        self.history = list()   # list of moves for each generation: [(p1_move, p2_move), (p1_move, p2_move), ...]
        self.agent_node = agent_node
        self.opponent = opponent

    def run(self):
        """ Runs a two player game between player_1 and player_2, and records their payoffs """

        new_moves = self.player_1.move(self, 0), self.player_2.move(self, 1)
        self.history.append(new_moves)
        self.player_1.record(self)
        self.player_2.record(self)

    def get_last_move(self, player):
        """ Returns last move for the agent player """

        last_move = None

        # find whether player is the row player or the column player
        if self.player_1 == player:
            player_idx = 0
        else:
            player_idx = 1

        # return the move for the above player
        if self.history:
            last_move = self.history[-1][player_idx]

        return last_move

    def payoffs(self):

        # generate a payoff pair for each game iteration in history
        payoffs = (self.game_matrix[m1][m2] for (m1, m2) in self.history)

        # transpose to get a payoff sequence for each player
        pay1, pay2 = zip(*payoffs)

        # return a mapping of each player to its mean payoff
        return {self.player_1: sum(pay1)/float(len(pay1)), self.player_2: sum(pay2)/float(len(pay2))}
