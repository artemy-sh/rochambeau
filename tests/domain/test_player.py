from rochambeau.domain.entities.enums import PlayerType
from rochambeau.domain.interfaces.player import IPlayer


def test_player_create(human_player: IPlayer, ai_player: IPlayer) -> None:
    """Checks that human and AI players are created with correct names and types."""
    assert human_player.player_name == "Human_1"
    assert human_player.player_type == PlayerType.HUMAN

    assert ai_player.player_name == "AI_1"
    assert ai_player.player_type == PlayerType.AI
