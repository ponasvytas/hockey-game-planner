from dash import dcc
from models import Game, Player, Strategy


def create_dummy_game():
    players = [
        Player("Ramune"),
        Player("Alba"),
        Player("Abby"),
        Player("Emma"),
        Player("Charlotte"),
        Player("Camille"),
        Player("Vivienne"),
        Player("Sami"),
        Player("Mackenna"),
    ]
    g = Game(players)

    enter = Strategy.CLRD
    exit_ = Strategy.CLRD

    for _ in range(31):
        # g.status()
        g.new_shift(enter, exit_)

    return g.summary()


summary_graph = dcc.Graph(id="summary-graph", figure=create_dummy_game())
