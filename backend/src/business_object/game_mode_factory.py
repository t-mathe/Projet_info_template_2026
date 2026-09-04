from business_object.game_mode import CoinFlipMode, DiceMode, Game_mode_enum, GameMode


class GameModeFactory:
    @classmethod
    def get_mode(cls, game_mode: Game_mode_enum) -> GameMode:
        """
        Returns the corresponding GameMode object.
        Args:
            game_mode (str): The identifier of the game mode (e.g., 'coinflip', 'dice').
        Returns:
            GameMode: An instance of a class implementing GameMode.
        Raises:
            ValueError: If the requested game_mode is not supported.
        """
        match game_mode:
            case Game_mode_enum.COINFLIP:
                return CoinFlipMode()
            case Game_mode_enum.DICE:
                return DiceMode()
