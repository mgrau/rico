from __future__ import division
from player import *
from numpy import *

class Simulation:
    def __init__(self, player_types, player_args=None):
        self.n_players = len(player_types)
        self.player_types = player_types
        if player_args is None:
            player_args = self.n_players*[None]
        self.player_args = player_args
        self.games = []

    def run_sim(self, N_games):
        for game_idx in xrange(N_games):
            players = [player_type(*player_arg) for (player_type, player_arg) in zip(self.player_types, self.player_args)]
            game = Game()
            game.players.extend(players)
            game.setup()
            while not game.game_end():
                game.round()
            self.games.append(game)
        self.point_res = self.point_results()
        return self.point_res

    def point_results(self):
        N = len(self.games)
        res = zeros((N,self.n_players))
        for game_idx, game in enumerate(self.games):
            for player_idx, player in enumerate(game.players):
                res[game_idx, player_idx] = player.points
        return res

    def win_results(self):
        res = self.point_res
        return argmax(res,1)

    def mean_point_results(self):
        res = self.point_res
        return mean(res,0)

    def net_win_results(self):
        w = self.win_results()
        res = zeros(self.n_players)
        for player_idx in xrange(self.n_players):
            res[player_idx] = sum(w==player_idx)
        return res





