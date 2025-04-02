import logging
import sys

from rochambeau.adapters.controllers.cli_controller import CliController
from rochambeau.adapters.loggers import (
    Logger,
    get_console_handler,
    get_file_handler,
)
from rochambeau.adapters.presenters.cli_presenter import CliPresenter
from rochambeau.adapters.providers.random_move_provider import (
    RandomMoveProvider,
)
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import GameMode
from rochambeau.domain.entities.game_settings import GameSettings


class DIContainer:
    """
    Dependency injection container for configuring and providing components.
    """

    def __init__(
        self,
        win_count: int = 5,
        game_mode: GameMode | None = None,
        log_level: int = logging.INFO,
    ):
        """
        Initializes container with game settings and logging configuration.
        """
        self._game_settings = GameSettings(win_count, game_mode)
        self._move_provider = RandomMoveProvider()
        self._log_level = log_level

    def move_provider(self) -> IMoveProvider:
        """
        Returns the move provider (default: random).
        """
        return self._move_provider

    def logger(self) -> ILogger:
        """
        Returns a configured logger with file and console handlers.
        """
        logger = Logger(level=self._log_level)
        logger.add_handler(
            get_file_handler(
                level=self._log_level, log_path="logs/rochambeau.log"
            )
        )
        logger.add_handler(
            get_console_handler(level=logging.ERROR, stream=sys.stderr)
        )
        return logger

    def cli_controller(self) -> CliController:
        """
        Returns the CLI controller with injected dependencies.
        """
        return CliController(
            self._game_settings, self.cli_presenter(), self.logger()
        )

    def cli_presenter(self) -> CliPresenter:
        """
        Returns the CLI presenter for formatting output.
        """
        return CliPresenter()
