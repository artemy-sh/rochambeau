from pytest import CaptureFixture, MonkeyPatch

from rochambeau.entrypoints.di import DIContainer


def test_cli_entrypoint(
    monkeypatch: MonkeyPatch,
    capsys: CaptureFixture[str],
) -> None:
    """Tests full CLI game flow via DI container and captures printed output."""
    inputs = iter(["hh", "Player_1", "Player_2", "R", "S"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    container = DIContainer(win_count=1)

    controller = container.cli_controller()
    game = controller.game_start()

    controller.game_play(game, None, None)

    output = capsys.readouterr().out

    assert "Game started!" in output
    assert "Player_1: ROCK vs Player_2: SCISSORS" in output
    assert "Winner: Player_1!" in output
    assert game.is_finished is True
