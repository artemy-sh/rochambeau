from rochambeau.adapters.providers.random_move_provider import (
    RandomMoveProvider,
)
from rochambeau.domain.entities.enums import Move


def test_random_move_provider() -> None:
    """Tests that RandomMoveProvider returns a valid Move."""
    assert RandomMoveProvider().get_move() in Move


def test_random_move_provider_all_moves() -> None:
    """Ensures RandomMoveProvider can return all possible moves over multiple runs."""
    provider = RandomMoveProvider()
    results = {provider.get_move() for _ in range(100)}

    assert results == set(Move)
