from business_object.game import Game_mode_enum
from business_object.game_mode_factory import GameModeFactory
from business_object.player import Player

p1 = Player(username="test1", elo=0, email="")
p2 = Player(username="test2", elo=0, email="")

game_mode = GameModeFactory.get_mode(Game_mode_enum.COINFLIP)
game = game_mode.play(p1, p2, "heads")
print(game)
print(game.description)

game_mode = GameModeFactory.get_mode(Game_mode_enum.DICE)
game = game_mode.play(p1, p2)
print(game)
print(game.description)
