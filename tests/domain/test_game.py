from rochambeau.domain.entities.enums import GameMode, Move
from rochambeau.domain.interfaces.game import IGame


def test_create_game(game_human_ai: IGame) -> None:
    """Checks game creation with correct players and mode."""
    assert game_human_ai.player1.player_name == "Human_1"
    assert game_human_ai.player2.player_name == "AI_1"
    assert game_human_ai.game_mode is GameMode.HUMAN_VS_AI


def test_move_round_draw(game_human_ai: IGame) -> None:
    """Player1 wins a round; score updates; game continues."""
    winner = game_human_ai.make_move(Move.ROCK, Move.SCISSORS)

    assert winner is game_human_ai.player1
    assert game_human_ai.scores[winner] == 1
    assert game_human_ai.is_finished is False


def test_round_win(game_human_ai: IGame) -> None:
    """Player1 wins a round and game is not finished."""
    winner = game_human_ai.make_move(Move.ROCK, Move.SCISSORS)

    assert winner is game_human_ai.player1
    assert game_human_ai.scores[winner] == 1
    assert game_human_ai.is_finished is False


def test_round_move_lose(game_human_ai: IGame) -> None:
    """Player1 loses a round; Player2 gets a point."""
    winner = game_human_ai.make_move(Move.ROCK, Move.PAPER)

    assert winner is game_human_ai.player2
    assert game_human_ai.scores[winner] == 1
    assert game_human_ai.is_finished is False


def test_move_lose(game_human_ai: IGame) -> None:
    """Losing round updates Player2’s score; game continues."""
    winner = game_human_ai.make_move(Move.ROCK, Move.PAPER)

    assert winner is game_human_ai.player2
    assert game_human_ai.scores[winner] == 1
    assert game_human_ai.is_finished is False


def test_game_winner_human(game_human_ai: IGame) -> None:
    """Player1 wins 3 rounds in a row; game ends."""
    winner = game_human_ai.make_move(Move.ROCK, Move.SCISSORS)
    winner = game_human_ai.make_move(Move.PAPER, Move.ROCK)
    winner = game_human_ai.make_move(Move.SCISSORS, Move.PAPER)

    assert game_human_ai.get_last_round() == (
        Move.SCISSORS,
        Move.PAPER,
        winner,
    )
    assert winner is game_human_ai.player1
    assert game_human_ai.scores[winner] == 3
    assert game_human_ai.is_finished is True
