import logging

import pytest

from rochambeau.adapters.controllers.cli_controller import CliController
from rochambeau.adapters.loggers.console_handler import get_console_handler
from rochambeau.adapters.loggers.logger import Logger
from rochambeau.adapters.presenters.cli_presenter import CliPresenter
from rochambeau.adapters.providers.random_move_provider import (
    RandomMoveProvider,
)
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import GameMode, PlayerType
from rochambeau.domain.entities.game import Game
from rochambeau.domain.entities.game_settings import GameSettings
from rochambeau.domain.entities.player import Player
from rochambeau.domain.interfaces.game import IGame
from rochambeau.domain.interfaces.player import IPlayer


@pytest.fixture
def human_player() -> IPlayer:
    """Returns a human player with the name 'Human_1'."""
    return Player("Human_1", PlayerType.HUMAN)


@pytest.fixture
def human_player_two() -> IPlayer:
    """Returns another human player with the name 'Human_2'."""
    return Player("Human_2", PlayerType.HUMAN)


@pytest.fixture
def ai_player() -> IPlayer:
    """Returns an AI player with the name 'AI_1'."""
    return Player("AI_1", PlayerType.AI)


@pytest.fixture
def game_settings() -> GameSettings:
    """Returns default game settings with 3 wins needed and Human vs AI mode."""
    return GameSettings(win_count=3, game_mode=GameMode.HUMAN_VS_AI)


@pytest.fixture
def game_human_ai(
    human_player: IPlayer, ai_player: IPlayer, game_settings: GameSettings
) -> IGame:
    """Returns a Game instance with a human and an AI player."""
    return Game(human_player, ai_player, game_settings)


@pytest.fixture
def game_human_human(
    human_player: IPlayer,
    human_player_two: IPlayer,
    game_settings: GameSettings,
) -> IGame:
    """Returns a Game instance with two human players."""
    return Game(human_player, human_player_two, game_settings)


@pytest.fixture
def random_move_provider() -> IMoveProvider:
    """Returns an instance of the random move provider."""
    return RandomMoveProvider()


@pytest.fixture
def logger() -> ILogger:
    """Returns a logger configured with a console handler."""
    logger = Logger(level=logging.INFO)
    logger.add_handler(get_console_handler())
    return logger


@pytest.fixture
def cli_controller(logger: ILogger) -> CliController:
    """Returns a CLI controller instance with basic game settings and presenter."""
    presenter = CliPresenter()
    game_settings = GameSettings(win_count=1)
    return CliController(game_settings, presenter, logger)
