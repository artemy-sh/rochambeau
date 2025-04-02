from unittest.mock import Mock

from rochambeau.adapters.presenters.cli_presenter import CliPresenter
from rochambeau.domain.entities.enums import Move


def test_cli_presenter_round_result() -> None:
    """Tests CLIPresenter output for a round where player1 wins."""
    presenter = CliPresenter()

    game_mock = Mock()
    game_mock.player1.player_name = "Player_1"
    game_mock.player2.player_name = "Player_2"
    game_mock.get_last_round.return_value = (
        Move.ROCK,
        Move.SCISSORS,
        game_mock.player1,
    )

    result = presenter.round_result(game_mock)

    assert "Player_1: ROCK vs Player_2: SCISSORS" in result
    assert "Winner: Player_1!" in result
