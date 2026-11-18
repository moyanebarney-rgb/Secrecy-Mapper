import pytest

from secrecy_mapper.models import Entity, Relationship
from secrecy_mapper.validation import validate_dataset


@pytest.fixture
def entities():
    return [
        Entity(
            entity_id="A",
            entity_type="organisation",
            name="Alpha Holdings",
        ),
        Entity(
            entity_id="B",
            entity_type="organisation",
            name="Beta Trading",
        ),
    ]


@pytest.fixture
def relationship():
    return Relationship(
        relationship_id="R001",
        source_id="A",
        target_id="B",
        relationship_type="ownership",
        evidence_id="E001",
        confidence="high",
        observed_at="2026-01-15",
    )


def test_valid_dataset_passes(entities, relationship):
    validate_dataset(entities, [relationship])


def test_duplicate_entity_ids_fail(entities, relationship):
    duplicate_entities = entities + [entities[0]]

    with pytest.raises(ValueError, match="Duplicate entity IDs"):
        validate_dataset(duplicate_entities, [relationship])


def test_duplicate_relationship_ids_fail(entities, relationship):
    with pytest.raises(ValueError, match="Duplicate relationship IDs"):
        validate_dataset(entities, [relationship, relationship])


def test_unknown_source_entity_fails(entities, relationship):
    relationship.source_id = "UNKNOWN"

    with pytest.raises(ValueError, match="Unknown source entity"):
        validate_dataset(entities, [relationship])


def test_unknown_target_entity_fails(entities, relationship):
    relationship.target_id = "UNKNOWN"

    with pytest.raises(ValueError, match="Unknown target entity"):
        validate_dataset(entities, [relationship])


def test_self_referencing_relationship_fails(entities, relationship):
    relationship.target_id = relationship.source_id

    with pytest.raises(ValueError, match="Self-referencing relationship"):
        validate_dataset(entities, [relationship])
