from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import GameMode, PlayerType
from rochambeau.domain.entities.game import Game
from rochambeau.domain.entities.game_settings import GameSettings
from rochambeau.domain.entities.player import Player
from rochambeau.domain.interfaces.game import IGame
from rochambeau.domain.interfaces.player import IPlayer


class StartGame:
    """
    Use case for starting a new game.
    """

    def __init__(self, game_settings: GameSettings, logger: ILogger):
        """
        Initializes the use case with settings and logger.
        """
        self._game_settings = game_settings
        self._logger: ILogger = logger

    def execute(
        self,
        player1_name: str,
        player2_name: str,
    ) -> IGame:
        """
        Runs the use case and returns a new Game instance.
        """
        self._logger.info("Starting a new game!")
        player1, player2 = self._create_players(
            self._game_settings.game_mode, player1_name, player2_name
        )
        self._logger.info(
            f"Players: {player1_name} ({player1.player_type.value}) vs {player2_name} ({player2.player_type.value})"
        )
        return Game(player1, player2, self._game_settings)

    def _create_players(
        self, game_mode: GameMode | None, player1_name: str, player2_name: str
    ) -> tuple[IPlayer, IPlayer]:
        """
        Creates players based on selected game mode.
        """
        self._logger.debug("Create players")
        if game_mode == GameMode.HUMAN_VS_HUMAN:
            player1 = Player(player1_name, PlayerType.HUMAN)
            player2 = Player(player2_name, PlayerType.HUMAN)
        elif game_mode == GameMode.HUMAN_VS_AI:
            player1 = Player(player1_name, PlayerType.HUMAN)
            player2 = Player(player2_name, PlayerType.AI)
        elif game_mode == GameMode.AI_VS_AI:
            player1 = Player(player1_name, PlayerType.AI)
            player2 = Player(player2_name, PlayerType.AI)
        else:
            self._logger.error(f"Invalid game mode provided: {game_mode}")
            raise ValueError("Invalid game mode provided!")

        return player1, player2
