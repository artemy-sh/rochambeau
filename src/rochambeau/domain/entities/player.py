from .enums import PlayerType


class Player:
    """
    Represents a game player (human or AI).
    """

    def __init__(
        self,
        name: str,
        player_type: PlayerType,
    ):
        """
        Initializes a player with name and type.
        """
        self._name: str = name
        self._type: PlayerType = player_type

    @property
    def player_name(self) -> str:
        """
        Player's display name.
        """
        return self._name

    @property
    def player_type(self) -> PlayerType:
        """
        Type of the player: HUMAN or AI.
        """
        return self._type
