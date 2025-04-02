from rochambeau.domain.entities.enums import GameMode, Move, Result
from rochambeau.domain.entities.game_settings import GameSettings
from rochambeau.domain.interfaces.player import IPlayer


class Game:
    """
    Core domain class representing a game session.
    """

    def __init__(
        self, player1: IPlayer, player2: IPlayer, settings: GameSettings
    ):
        """
        Initialize a new game session.
        """
        self._player1: IPlayer = player1
        self._player2: IPlayer = player2
        self._settings: GameSettings = settings
        self._finished: bool = False
        self._rounds: list[tuple[Move, Move, IPlayer | None]] = []
        self._scores: dict[IPlayer, int] = {self._player1: 0, self._player2: 0}

    @property
    def is_finished(self) -> bool:
        """
        True if any player reached the required number of wins.
        """
        return self._finished

    @property
    def player1(self) -> IPlayer:
        """
        First player instance.
        """
        return self._player1

    @property
    def player2(self) -> IPlayer:
        """
        Second player instance.
        """
        return self._player2

    @property
    def game_mode(self) -> GameMode | None:
        """
        Game mode (e.g. HUMAN_VS_AI).
        """
        return self._settings.game_mode

    @property
    def scores(self) -> dict[IPlayer, int]:
        """
        Current score for both players.
        """
        return self._scores

    def get_last_round(self) -> tuple[Move, Move, IPlayer | None]:
        """
        Returns the last played round.
        """
        return self._rounds[-1]

    def make_move(
        self, player1_move: Move, player2_move: Move
    ) -> IPlayer | None:
        """
        Plays a round and updates the score.

        Returns:
            The winner of the round, or None if it's a draw.
        """
        result_move = self._determine_winner(player1_move, player2_move)
        if result_move is Result.WIN:
            winner = self._player1
        elif result_move is Result.LOSE:
            winner = self._player2
        else:
            winner = None

        if winner:
            self._scores[winner] += 1

        self._rounds.append((player1_move, player2_move, winner))

        if self._check_finished():
            self._finished = True

        return winner

    def _check_finished(self) -> bool:
        """
        Returns True if any player has reached the win count.
        """
        return any(
            score >= self._settings.win_count
            for score in self._scores.values()
        )

    def _determine_winner(self, move1: Move, move2: Move) -> Result:
        """
        Determines the outcome of a round based on two moves.
        """
        rules: dict[Move, Move] = {
            Move.ROCK: Move.SCISSORS,
            Move.PAPER: Move.ROCK,
            Move.SCISSORS: Move.PAPER,
        }

        if move1 == move2:
            return Result.DRAW

        return Result.WIN if rules[move1] == move2 else Result.LOSE
