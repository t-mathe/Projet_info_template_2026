from datetime import datetime

from business_object.game import Game, Game_mode_enum
from business_object.player import Player

truc = Game(
    p1=Player(username="test1", elo=0, email=""),
    p2=Player(username="test1", elo=0, email=""),
    game_mode=Game_mode_enum.COINFLIP,
    winner=None,
    description="",
    timestamp=datetime.now(),
)

print(truc)
