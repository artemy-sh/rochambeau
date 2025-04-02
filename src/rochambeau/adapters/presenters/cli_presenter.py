from rochambeau.domain.interfaces.game import IGame


class CliPresenter:
    """
    Formats game data for CLI output.
    """

    def round_result(self, game: IGame) -> str:
        player1_move, player2_move, winner = game.get_last_round()
        result = (
            f"{game.player1.player_name}: {player1_move.value} vs "
            f"{game.player2.player_name}: {player2_move.value}\n"
        )
        result += f"Winner: {winner.player_name}!" if winner else "Draw!"
        return result

    def game_finished(self, game: IGame) -> str:
        """
        Returns a formatted string showing final game result and score.
        """
        _, _, winner = game.get_last_round()
        result_text = (
            winner.player_name + " wins the game!" if winner else "It is Draw!"
        )
        score1 = game.scores[game.player1]
        score2 = game.scores[game.player2]
        return (
            f"Game over! {result_text}\n"
            f"Final score: {game.player1.player_name} ({score1} - {score2}) {game.player2.player_name}"
        )
