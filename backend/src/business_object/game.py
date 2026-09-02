from datetime import datetime
from enum import Enum

from business_object.player import Player


class Game_mode_enum(Enum):
    COINFLIP = "coinflip"
    DICE = "dice"


class Game:
    def __init__(
        self,
        p1: Player,
        p2: Player,
        game_mode: Game_mode_enum,
        winner: [Player | None],
        description: str,
        timestamp: datetime,
        id: int = None,
    ):
        self.id_game = id
        self.player1 = p1
        self.player2 = p2
        self.game_mode = game_mode
        self.winner = winner
        self.description = description
        self.timestamp = timestamp

    def __str__(self):
        desc1 = (
            f"{self.game_mode.value} between {self.player1.username} and {self.player2.username}."
        )
        desc2 = f"{self.winner.id_player}" if self.winner is not None else ""
        return desc1 + desc2
