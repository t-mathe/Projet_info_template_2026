from abc import ABC, abstractmethod
from datetime import datetime
from secrets import choice
from typing import Literal

from src.business_object.game import Game, Game_mode_enum
from src.business_object.player import Player


class GameMode(ABC):
    @abstractmethod
    def play(p1: Player, p2: Player) -> Game:
        pass


class DiceMode(GameMode):
    def play(p1: Player, p2: Player) -> Game:
        d1 = choice(range(1, 7))
        d2 = choice(range(1, 7))
        if d1 > d2:
            winner = p1
        elif d1 < d2:
            winner = p2
        else:
            winner = None
        return Game(p1, p2, Game_mode_enum.DICE, winner, "", datetime.now())


class CoinFlipMode(GameMode):
    def play(p1: Player, p2: Player, choise: Literal["heads" | "tails"]) -> Game:
        result = choice(["heads", "tails"])
        winner = p1 if result == choice else p2
        return Game(p1, p2, Game_mode_enum.DICE, winner, "", datetime.now())
