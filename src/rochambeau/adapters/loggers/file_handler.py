import logging
from pathlib import Path


def get_file_handler(
    level: int = logging.INFO,
    log_path: str = "logs/rochambeau.log",
) -> logging.Handler:
    """
    Creates a file handler for logging.
    """
    Path(log_path).parent.mkdir(parents=True, exist_ok=True)
    handler = logging.FileHandler(log_path, encoding="utf-8")
    handler.setLevel(level)
    formatter = logging.Formatter(
        fmt="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%d-%m-%y %H:%M:%S",
    )
    handler.setFormatter(formatter)
    return handler
