import pytest

from rochambeau.application.interactors.start_game import StartGame
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import GameMode, PlayerType
from rochambeau.domain.entities.game_settings import GameSettings


def test_start_game_human_ai(
    game_settings: GameSettings, logger: ILogger
) -> None:
    """Starts game in HUMAN vs AI mode; checks player names and types."""
    game = StartGame(game_settings, logger).execute("Human_1", "AI_1")

    assert game.player1.player_name == "Human_1"
    assert game.player2.player_name == "AI_1"
    assert game.player1.player_type is PlayerType.HUMAN
    assert game.player2.player_type is PlayerType.AI


def test_start_game_human_human(
    game_settings: GameSettings, logger: ILogger
) -> None:
    """Starts game in HUMAN vs HUMAN mode; verifies both players are human."""
    game_settings.game_mode = GameMode.HUMAN_VS_HUMAN
    game = StartGame(game_settings, logger).execute("Human_1", "Human_2")

    assert game.player1.player_name == "Human_1"
    assert game.player2.player_name == "Human_2"
    assert game.player1.player_type is PlayerType.HUMAN
    assert game.player2.player_type is PlayerType.HUMAN


def test_start_game_ai_ai(
    game_settings: GameSettings, logger: ILogger
) -> None:
    """Starts game in AI vs AI mode; verifies both players are AI."""
    game_settings.game_mode = GameMode.AI_VS_AI
    game = StartGame(game_settings, logger).execute("AI_1", "AI_2")

    assert game.player1.player_name == "AI_1"
    assert game.player2.player_name == "AI_2"
    assert game.player1.player_type is PlayerType.AI
    assert game.player2.player_type is PlayerType.AI


def test_start_undefined(game_settings: GameSettings, logger: ILogger) -> None:
    """Raises ValueError if game mode is not defined."""
    game_settings.game_mode = None

    with pytest.raises(ValueError, match="Invalid game mode provided!"):
        assert StartGame(game_settings, logger).execute("AI_1", "AI_2")
