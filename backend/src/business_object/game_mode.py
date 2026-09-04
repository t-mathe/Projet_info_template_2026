from abc import ABC, abstractmethod
from datetime import datetime
from secrets import choice
from typing import Literal

from business_object.game import Game, Game_mode_enum
from business_object.player import Player


class GameMode(ABC):
    @abstractmethod
    def play(self, p1: Player, p2: Player) -> Game:
        pass


class DiceMode(GameMode):
    def play(self, p1: Player, p2: Player) -> Game:
        d1 = choice(range(1, 7))
        d2 = choice(range(1, 7))
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None
        desc = f"{p1.username}:{d1} - {p2.username}:{d2} : {winner.username} won."
        return Game(p1, p2, Game_mode_enum.DICE, winner, desc, datetime.now())


class CoinFlipMode(GameMode):
    def play(self, p1: Player, p2: Player, side: Literal["heads", "tails"]) -> Game:
        result = choice(["heads", "tails"])
        winner = p1 if result == side else p2
        desc = f"{p1.username} chose {side}, coin said {result}, {winner.username} won."
        return Game(p1, p2, Game_mode_enum.DICE, winner, desc, datetime.now())
