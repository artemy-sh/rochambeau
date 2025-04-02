from pytest import MonkeyPatch

from rochambeau.adapters.controllers.cli_controller import CliController
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.domain.entities.enums import GameMode, Move, PlayerType


def test_cli_controller_game_start(
    cli_controller: CliController,
    monkeypatch: MonkeyPatch,
) -> None:
    """Tests CLI game start in HUMAN vs AI mode using user input."""
    inputs = iter(["ha", "Player_test"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = cli_controller.game_start()

    assert game.player1.player_name == "Player_test"
    assert game.player2.player_name == "AI_2"
    assert game.player1.player_type is PlayerType.HUMAN
    assert game.player2.player_type is PlayerType.AI
    assert game.game_mode == GameMode.HUMAN_VS_AI


def test_cli_controller_game_play_hh(
    cli_controller: CliController,
    monkeypatch: MonkeyPatch,
) -> None:
    """Tests CLI game play in HUMAN vs HUMAN mode with two players' moves."""
    inputs = iter(["hh", "Player_1", "Player_2", "R", "S"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = cli_controller.game_start()

    cli_controller.game_play(game, None, None)

    assert game.get_last_round() == (Move.ROCK, Move.SCISSORS, game.player1)
    assert game.is_finished is True


def test_cli_controller_game_play_ha(
    cli_controller: CliController,
    monkeypatch: MonkeyPatch,
    random_move_provider: IMoveProvider,
) -> None:
    """Tests CLI game play in HUMAN vs AI mode with random move for AI."""
    inputs = iter(["ha", "Player_test", "R"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs, "R"))

    game = cli_controller.game_start()

    cli_controller.game_play(game, None, random_move_provider)

    _, _, result = game.get_last_round()
    assert result in (game.player1, game.player2)
    assert game.is_finished is True


def test_cli_controller_game_play_aa(
    cli_controller: CliController,
    monkeypatch: MonkeyPatch,
    random_move_provider: IMoveProvider,
) -> None:
    """Tests CLI game play in AI vs AI mode using random moves for both players."""
    inputs = iter(["aa"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    game = cli_controller.game_start()

    cli_controller.game_play(game, random_move_provider, random_move_provider)

    _, _, result = game.get_last_round()
    assert result in (game.player1, game.player2)
    assert game.is_finished is True
