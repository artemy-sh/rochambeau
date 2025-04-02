from typing import Protocol

from rochambeau.domain.entities.enums import PlayerType


class IPlayer(Protocol):
    """
    Player interface tha represents a game player (human or AI).
    """

    def __init__(
        self,
        name: str,
        player_type: PlayerType,
    ):
        """
        Initializes a player with name and type.
        """
        ...

    @property
    def player_name(self) -> str:
        """
        Player's display name.
        """
        ...

    @property
    def player_type(self) -> PlayerType:
        """
        Type of the player: HUMAN or AI.
        """
        ...
