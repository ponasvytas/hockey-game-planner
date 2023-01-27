import pytest

from src.models import Bench, Player, Position, Game, Strategy


class TestBench:
    def test_create_bench(self):

        b = Bench()

        p1 = Player("Vytas", Position.CENTER)

        b.players.append(p1)

        assert len(b.players) == 1


class TestGame:
    def test_play_one_shift(self):
        goalie = Player("Amelia")

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

        g = Game(players=players)

        enter = Strategy.CLRD
        exit_ = Strategy.CLRD

        print("Game start!")
        for _ in range(31):
            g.status()
            g.new_shift(enter, exit_)

        g.summary()