import argparse
import logging
from argparse import Namespace


def parse_log_level(level: str) -> int:
    """
    Parses a string log level into a logging constant.
    """
    levels = {
        "debug": logging.DEBUG,
        "info": logging.INFO,
        "warning": logging.WARNING,
        "error": logging.ERROR,
    }
    level_upper = level.upper()
    if level_upper not in levels:
        raise argparse.ArgumentTypeError(f"Invalid log level: {level}")
    return levels[level_upper]


def positive_int(x: str) -> int:
    """
    Validates that a CLI argument is a positive integer.
    """
    y = int(x)
    if y <= 0:
        raise argparse.ArgumentTypeError("Number of rounds must be at least 1")
    return y


def parse_args() -> Namespace:
    """
    Parses CLI arguments for the game configuration.
    """
    parser = argparse.ArgumentParser(description="Play Rochambeau CLI Game")

    parser.add_argument(
        "--mode",
        type=str,
        choices=["hh", "ha", "aa", "manual"],
        default="manual",
        metavar="MODE",
        help="Game mode: hh (human vs human), ha (human vs AI), aa (AI vs AI), manual (manual input mode)",
    )
    parser.add_argument(
        "--rounds",
        type=positive_int,
        default=5,
        metavar="ROUNDS",
        help="Number of wins needed to finish the game",
    )
    parser.add_argument(
        "--log-level",
        type=parse_log_level,
        default=logging.INFO,
        metavar="LEVEL",
        help="Logging level: debug, info, warning, error",
    )
    return parser.parse_args()
