from typing import Protocol

from rochambeau.domain.entities.enums import GameMode, Move
from rochambeau.domain.entities.game_settings import GameSettings
from rochambeau.domain.interfaces.player import IPlayer


class IGame(Protocol):
    """
    Game interface that defines core methods and properties for game logic.
    """

    def __init__(
        self, player1: IPlayer, player2: IPlayer, settings: GameSettings
    ): ...

    @property
    def is_finished(self) -> bool:
        """
        True if any player reached the required number of wins.
        """
        ...

    @property
    def player1(self) -> IPlayer:
        """
        First player.
        """
        ...

    @property
    def player2(self) -> IPlayer:
        """
        Second player.
        """
        ...

    @property
    def game_mode(self) -> GameMode | None:
        """
        Current game mode.
        """
        ...

    @property
    def scores(self) -> dict[IPlayer, int]:
        """
        Scoreboard for each player.
        """
        ...

    def get_last_round(self) -> tuple[Move, Move, IPlayer | None]:
        """
        Returns the last played round.
        """
        ...

    def make_move(
        self, player1_move: Move, player2_move: Move
    ) -> IPlayer | None:
        """
        Plays a round and updates the score.

        Returns:
            The winner of the round, or None if it's a draw.
        """
        ...
