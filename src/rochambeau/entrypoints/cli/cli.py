from argparse import Namespace

from rochambeau.domain.entities.enums import GameMode
from rochambeau.entrypoints.cli.parse_args import parse_args
from rochambeau.entrypoints.di import DIContainer


def entrypoint() -> None:
    """
    Entry point for running the CLI game.
    """
    args: Namespace = parse_args()

    short_game_mode = {
        "hh": GameMode.HUMAN_VS_HUMAN,
        "ha": GameMode.HUMAN_VS_AI,
        "aa": GameMode.AI_VS_AI,
        "manual": None,
    }

    container = DIContainer(
        win_count=args.rounds,
        game_mode=short_game_mode[args.mode],
        log_level=args.log_level,
    )

    controller = container.cli_controller()
    game = controller.game_start()

    random_move_provider = container.move_provider()
    player1_move_provider = random_move_provider
    player2_move_provider = random_move_provider

    controller.game_play(game, player1_move_provider, player2_move_provider)
