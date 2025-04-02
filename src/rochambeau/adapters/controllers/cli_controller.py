import time

from rochambeau.adapters.presenters.cli_presenter import CliPresenter
from rochambeau.application.interactors.play_round import PlayRound
from rochambeau.application.interactors.start_game import StartGame
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import GameMode, Move
from rochambeau.domain.entities.game_settings import GameSettings
from rochambeau.domain.interfaces.game import IGame


class CliController:
    """
    CLI controller for managing game flow and user interaction.
    """

    def __init__(
        self,
        game_settings: GameSettings,
        presenter: CliPresenter,
        logger: ILogger,
    ):
        """
        Initializes the controller with settings, presenter, and logger.
        """
        self._presenter = presenter
        self._game_settings = game_settings
        self._logger = logger

    def game_start(self) -> IGame:
        """
        Starts a new game session and returns a Game instance.
        """
        print("Game started!")

        if not self._game_settings.game_mode:
            self._game_settings.game_mode = self._select_mode()

        player1_name = "AI_1"
        player2_name = "AI_2"

        if self._game_settings.game_mode in (
            GameMode.HUMAN_VS_HUMAN,
            GameMode.HUMAN_VS_AI,
        ):
            player1_name = (
                input("\nEnter Player 1 name (default: Player_1): ")
                or "Player_1"
            )
        if self._game_settings.game_mode is GameMode.HUMAN_VS_HUMAN:
            player2_name = (
                input("\nEnter Player 2 name (default: Player_2): ")
                or "Player_2"
            )

        try:
            return StartGame(self._game_settings, self._logger).execute(
                player1_name, player2_name
            )
        except ValueError as e:
            print(f"\nError starting game: {e}")
            exit(1)

    def _select_mode(self) -> GameMode:
        """
        Prompts the user to select a game mode from the console.
        """
        short_game_mode = {
            "hh": GameMode.HUMAN_VS_HUMAN,
            "ha": GameMode.HUMAN_VS_AI,
            "aa": GameMode.AI_VS_AI,
        }
        select_game_mode = ""

        while True:
            select_game_mode = (
                input(
                    "\nSelect game mode:\n"
                    "  hh - Human vs Human\n"
                    "  ha - Human vs AI\n"
                    "  aa - AI vs AI\n\n"
                    "Enter your choice: "
                )
                .strip()
                .lower()
            )
            if select_game_mode in short_game_mode.keys():
                break
            else:
                print("\nInvalid game mode selected, please try again.")
                time.sleep(1)

        return short_game_mode[select_game_mode]

    def game_play(
        self,
        game: IGame,
        player1_move_provider: IMoveProvider | None,
        player2_move_provider: IMoveProvider | None,
    ) -> None:
        """
        Runs the main game loop and plays rounds until the game is finished.
        """
        play_round = PlayRound(
            game, self._logger, player1_move_provider, player2_move_provider
        )
        player1_move = None
        player2_move = None
        winner = None

        while not game.is_finished:
            if game.game_mode in [
                GameMode.HUMAN_VS_AI,
                GameMode.HUMAN_VS_HUMAN,
            ]:
                player1_move = self._select_move(game.player1.player_name)
            else:
                time.sleep(1)

            if game.game_mode is GameMode.HUMAN_VS_HUMAN:
                player2_move = self._select_move(game.player2.player_name)

            try:
                winner = play_round.execute(player1_move, player2_move)
            except ValueError as e:
                print(f"\nError: {e}")
                self._logger.error(f"Failed round: {e}")
                break

            print("\n" + self._presenter.round_result(game))

        if winner is not None:
            print("\n" + self._presenter.game_finished(game) + "\n")
        else:
            self._logger.error("Unexpected: game finished without a winner")

    def _select_move(self, player_name: str) -> Move:
        """
        Prompts a human player to select a move from the console.
        """
        while True:
            short_move = {
                "R": Move.ROCK,
                "P": Move.PAPER,
                "S": Move.SCISSORS,
            }
            select_move = (
                input(
                    f"\n{player_name}, select your move (R for Rock, P for Paper, S for Scissors): "
                )
                .strip()
                .upper()
            )
            if select_move in short_move:
                return short_move[select_move]
            else:
                print("\nInvalid choice, please select R, P, or S.")
