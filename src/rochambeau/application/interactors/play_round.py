from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import Move, PlayerType
from rochambeau.domain.interfaces.game import IGame
from rochambeau.domain.interfaces.player import IPlayer


class PlayRound:
    """
    Use case for playing one round of the game.
    """

    def __init__(
        self,
        game: IGame,
        logger: ILogger,
        player1_move_provider: IMoveProvider | None = None,
        player2_move_provider: IMoveProvider | None = None,
    ):
        """
        Initializes the round with game state and move providers.
        """
        self._game = game
        self._player1_move_provider = player1_move_provider
        self._player2_move_provider = player2_move_provider
        self._logger = logger

    def execute(
        self,
        player1_move: Move | None = None,
        player2_move: Move | None = None,
    ) -> IPlayer | None:
        """
        Runs the round and returns the winner or None if draw.
        """
        if self._game.is_finished:
            self._logger.error("The game is finished!")
            raise ValueError("The game is finished!")

        move1 = self._get_move(
            player1_move,
            self._game.player1.player_type,
            self._player1_move_provider,
        )
        move2 = self._get_move(
            player2_move,
            self._game.player2.player_type,
            self._player2_move_provider,
        )
        winner = self._game.make_move(move1, move2)

        self._logger.info(
            f"Round: {self._game.player1.player_name}({move1.value}) vs "
            f"{self._game.player2.player_name}({move2.value}) → "
            f"{'Winner: ' + winner.player_name if winner else 'Draw'}"
        )

        return winner

    def _get_move(
        self,
        player_move: Move | None,
        player_type: PlayerType,
        player_move_provider: IMoveProvider | None,
    ) -> Move:
        """
        Returns move for a player, either from input or provider.
        """
        if player_type == PlayerType.HUMAN:
            if player_move:
                return player_move
            else:
                self._logger.error("Player has not provided a move")
                raise ValueError("Player has not provided a move")
        elif player_type == PlayerType.AI:
            if player_move_provider:
                return player_move_provider.get_move()
            else:
                self._logger.error("Move provider is not provided")
                raise ValueError("Move provider is not provided")
