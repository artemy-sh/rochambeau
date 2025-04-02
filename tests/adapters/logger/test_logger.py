import logging
from io import StringIO
from pathlib import Path

from rochambeau.adapters.loggers import (
    Logger,
    get_console_handler,
    get_file_handler,
)


def test_logger_writes_info_message_to_stream() -> None:
    """Tests that Logger writes an INFO message to the given stream."""
    stream = StringIO()
    handler = get_console_handler(level=logging.INFO, stream=stream)

    logger = Logger(level=logging.INFO)
    logger.add_handler(handler)

    logger.info("Test message")
    logger.debug("Test debug")

    stream.seek(0)
    output = stream.read()
    assert "Test message" in output
    assert "INFO" in output
    assert "DEBUG" not in output


def test_logger_writes_to_file(tmp_path: Path) -> None:
    """Tests that Logger writes an INFO message to a log file."""
    log_file = tmp_path / "test.log"
    handler = get_file_handler(level=logging.INFO, log_path=str(log_file))

    logger = Logger(level=logging.INFO)
    logger.add_handler(handler)

    logger.info("Test log to file")
    logger.debug("Test debug")

    with log_file.open("r", encoding="utf-8") as f:
        content = f.read()
        assert "Test log to file" in content
        assert "INFO" in content
        assert "DEBUG" not in content
