import random
from dataclasses import dataclass, field
from collections import deque
from enum import StrEnum
from copy import deepcopy


import pandas as pd
import plotly.express as px


class Position(StrEnum):
    CENTER = "center"
    LEFT_WING = "left_wing"
    RIGHT_WING = "right_wing"
    DEFENCE = "defence"
    NONE = "none"


@dataclass
class Player:
    name: str
    position: Position = Position.NONE
    play_time: float = 0.0


class Bench:
    players: deque[Player] = deque()

    def __repr__(self) -> str:
        return f"Bench: {[p.name for p in self.players]}"


@dataclass
class Line:
    players: dict[Position, Player] = field(default_factory=dict)

    def __repr__(self):
        return f"Line {[(k.name, v.name) for k, v in self.players.items()]}"


class Strategy:
    CLRD = [Position.CENTER, Position.LEFT_WING, Position.RIGHT_WING, Position.DEFENCE]
    RLDC = [Position.RIGHT_WING, Position.LEFT_WING, Position.DEFENCE, Position.CENTER]
    DRLC = [Position.DEFENCE, Position.RIGHT_WING, Position.LEFT_WING, Position.CENTER]
    RLCD = [Position.RIGHT_WING, Position.LEFT_WING, Position.CENTER, Position.DEFENCE]


class Game:
    played_lines: list[Line] = []
    current_line: Line = Line()
    bench: Bench = Bench()
    players: list[Player] = []

    def __init__(self, players: list[Player], shuffle_start=True):

        self.players = sorted(players, key=lambda p: p.name)

        if shuffle_start:
            random.shuffle(players)

        for p in players:
            self.bench.players.append(p)

    def new_shift(
        self,
        enter_strategy: list[Position],
        exit_strategy: list[Position],
        shift_length=90,
    ):

        # new line for next shift
        new_line = Line()

        # new players on ince
        for pos in enter_strategy:
            player = self.bench.players.popleft()
            player.position = pos
            new_line.players[pos] = player
            player.play_time += shift_length

        # players going to bench
        if self.current_line.players:
            for pos in exit_strategy:
                p = self.current_line.players.pop(pos)
                p.position = Position.NONE
                self.bench.players.append(p)

        self.current_line = new_line
        self.played_lines.append(deepcopy(new_line))

    def status(self):
        print("===================")
        print(self.current_line)
        print(self.bench)

    def create_played_df(self):
        items = []
        for i, line in enumerate(self.played_lines):
            for pos, p in line.players.items():
                player_item = {"shift": i, "name": p.name, "position": pos}
                items.append(player_item)

        df = pd.DataFrame(items)
        return df

    def summary(self):

        df = self.create_played_df()
        df.sort_values("name", inplace=True)

        # fig = px.density_heatmap(df, x="name", y="position")
        # fig = px.bar(df, x="name", color="position")
        fig = px.histogram(df, x="name", color="position", histfunc="count")
        fig.update_layout(legend=dict(orientation="h", yanchor="top", y=1.10, title=""))

        return fig
