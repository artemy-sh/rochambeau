from dataclasses import dataclass

from .enums import GameMode


@dataclass
class GameSettings:
    """
    Game configuration settings:

    - win_count: Number of wins required to finish the game.
    - game_mode: Selected game mode. Can be None if set manually later.
    """

    win_count: int = 5
    game_mode: GameMode | None = None
