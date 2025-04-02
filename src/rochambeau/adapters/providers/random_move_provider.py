import random

from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.domain.entities.enums import Move


class RandomMoveProvider(IMoveProvider):
    """
    Provides a random move from the available options.
    """

    def get_move(self) -> Move:
        """
        Returns a randomly chosen move.
        """
        return random.choice(list(Move))
