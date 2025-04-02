from typing import Protocol, runtime_checkable

from rochambeau.domain.entities.enums import Move


@runtime_checkable
class IMoveProvider(Protocol):
    """
    Interface for AI move providers.
    """

    def get_move(self) -> Move:
        """
        Returns the next move for the AI player.
        """
        ...
