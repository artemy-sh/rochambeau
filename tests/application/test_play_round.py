import pytest

from rochambeau.application.interactors.play_round import PlayRound
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.domain.entities.enums import Move
from rochambeau.domain.interfaces.game import IGame


def test_play_round_human_human(
    game_human_human: IGame, logger: ILogger
) -> None:
    """Tests playing several rounds in HUMAN vs HUMAN mode with explicit moves."""
    play_round = PlayRound(game_human_human, logger)

    with pytest.raises(ValueError, match="Player has not provided a move"):
        assert play_round.execute(Move.PAPER, None) is game_human_human.player1

    assert (
        play_round.execute(Move.ROCK, Move.SCISSORS)
        is game_human_human.player1
    )
    assert (
        play_round.execute(Move.ROCK, Move.PAPER) is game_human_human.player2
    )
    assert play_round.execute(Move.ROCK, Move.ROCK) is None
    assert (
        play_round.execute(Move.PAPER, Move.ROCK) is game_human_human.player1
    )
    assert (
        play_round.execute(Move.PAPER, Move.ROCK) is game_human_human.player1
    )

    with pytest.raises(ValueError, match="The game is finished!"):
        assert (
            play_round.execute(Move.PAPER, Move.ROCK)
            is game_human_human.player1
        )


def test_play_round_human_ai(
    game_human_ai: IGame, random_move_provider: IMoveProvider, logger: ILogger
) -> None:
    """Tests playing rounds in HUMAN vs AI mode with and without a move provider."""
    play_round = PlayRound(game_human_ai, logger)

    with pytest.raises(ValueError, match="Move provider is not provided"):
        assert play_round.execute(Move.PAPER, None) is game_human_ai.player1

    play_round = PlayRound(game_human_ai, logger, None, random_move_provider)

    assert play_round.execute(Move.ROCK) in (
        game_human_ai.player1,
        game_human_ai.player2,
        None,
    )
