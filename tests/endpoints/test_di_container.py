from rochambeau.adapters.controllers.cli_controller import CliController
from rochambeau.adapters.presenters.cli_presenter import CliPresenter
from rochambeau.application.ports.move_provider import IMoveProvider
from rochambeau.application.services.logger import ILogger
from rochambeau.entrypoints.di import DIContainer


def test_di_container() -> None:
    """Tests that DIContainer provides correct component instances."""
    container = DIContainer()

    presenter = container.cli_presenter()
    controller = container.cli_controller()
    move_provider = container.move_provider()
    logger = container.logger()

    assert isinstance(controller, CliController)
    assert isinstance(presenter, CliPresenter)
    assert isinstance(move_provider, IMoveProvider)
    assert isinstance(logger, ILogger)
