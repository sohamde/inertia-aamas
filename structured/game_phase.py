import two_player_game as tpg
import globals as g
import random as rnd
rnd.seed()


def game_phase():
    """ Runs the game phase; saves actions and payoffs of each agent involved """

    # will keep track of the number of cooperators and defectors in the game phase
    num_normA = num_normB = 0

    if g.games_per_round > 0:

        for num_games in range(g.games_per_round):

            # randomly permuting the agents
            rnd.shuffle(g.nodes_with_agents)

            # for each current agent on the network
            for agent_node in g.nodes_with_agents:

                # if the number of games played is less than or equal to num_games
                if len(g.network.node[agent_node]['agent'].games_played) <= num_games:

                    # find neighbors of the agent on agent_node; agent_neighbors contains neighbors with agents on them
                    agent_neighbors = g.neighbors_with_agents[agent_node]

                    # if an agent has no agents on it's neighbors, it won't play any games
                    if not agent_neighbors:
                        continue

                    # find neighbors who have played less than or equal to num_games
                    candidate_neighbors = [neighbor for neighbor in agent_neighbors
                                        if len(g.network.node[neighbor]['agent'].games_played) <= num_games]

                    # selecting neighbor to play against
                    if len(candidate_neighbors) > 0:
                        opponent = rnd.choice(candidate_neighbors)
                    else:
                        opponent = rnd.choice(agent_neighbors)

                    # create and run a new game
                    game = tpg.TwoPlayerGame(g.network.node[agent_node]['agent'], g.network.node[opponent]['agent'],
                                    g.game_matrix, g.game_actions, agent_node, opponent)
                    game.run()

                    # last move for row player - agent
                    if game.get_last_move(g.network.node[agent_node]['agent']) == 0:
                        num_normA += 1.0
                    else:
                        num_normB += 1.0

                    # last move for column player - opponent
                    if game.get_last_move(g.network.node[opponent]['agent']) == 0:
                        num_normA += 1.0
                    else:
                        num_normB += 1.0

                    g.normA_percentage = num_normA / (num_normA + num_normB)

                    # record payoffs
                    g.network.node[agent_node]['agent'].payoff += game.payoffs()[g.network.node[agent_node]['agent']]
                    g.network.node[opponent]['agent'].payoff += game.payoffs()[g.network.node[opponent]['agent']]

    # pair all neighbors if games_per_round = 0
    elif g.games_per_round == 0:

        # list of agents already considered
        considered_agents = list()

        rnd.shuffle(g.nodes_with_agents)

        # for each current agent on the network
        for agent_node in g.nodes_with_agents:

            # find neighbors of agent
            agent_neighbors = g.neighbors_with_agents[agent_node]

            # playing a game against each neighbor
            for opponent in agent_neighbors:

                if opponent not in considered_agents:

                    # create and run a new game
                    game = tpg.TwoPlayerGame(g.network.node[agent_node]['agent'], g.network.node[opponent]['agent'],
                                        g.game_matrix, g.game_actions, agent_node, opponent)
                    game.run()

                    # last move for row player - agent
                    if game.get_last_move(g.network.node[agent_node]['agent']) == 0:
                        num_normA += 1.0
                    else:
                        num_normB += 1.0

                    # last move for column player - opponent
                    if game.get_last_move(g.network.node[opponent]['agent']) == 0:
                        num_normA += 1.0
                    else:
                        num_normB += 1.0

                    g.normA_percentage = num_normA / (num_normA + num_normB)

                    # record payoffs
                    g.network.node[agent_node]['agent'].payoff += game.payoffs()[g.network.node[agent_node]['agent']]
                    g.network.node[opponent]['agent'].payoff += game.payoffs()[g.network.node[opponent]['agent']]

            # adding to list of already considered agents
            considered_agents.append(agent_node)

    # list of payoffs to agents
    for v in g.nodes_with_agents:
        agent = g.network.node[v].get('agent')
        g.payoff_list.append(agent.payoff)
