from collections import Counter

from secrecy_mapper.models import Entity, Relationship


def validate_dataset(
    entities: list[Entity],
    relationships: list[Relationship],
) -> None:
    """Validate entity and relationship integrity."""

    entity_ids = [entity.entity_id for entity in entities]
    relationship_ids = [
        relationship.relationship_id
        for relationship in relationships
    ]

    duplicate_entities = [
        entity_id
        for entity_id, count in Counter(entity_ids).items()
        if count > 1
    ]

    duplicate_relationships = [
        relationship_id
        for relationship_id, count in Counter(relationship_ids).items()
        if count > 1
    ]

    if duplicate_entities:
        raise ValueError(
            f"Duplicate entity IDs: {duplicate_entities}"
        )

    if duplicate_relationships:
        raise ValueError(
            f"Duplicate relationship IDs: {duplicate_relationships}"
        )

    known_entity_ids = set(entity_ids)

    for relationship in relationships:

        if relationship.source_id not in known_entity_ids:
            raise ValueError(
                f"Unknown source entity: {relationship.source_id}"
            )

        if relationship.target_id not in known_entity_ids:
            raise ValueError(
                f"Unknown target entity: {relationship.target_id}"
            )

        if relationship.source_id == relationship.target_id:
            raise ValueError(
                f"Self-referencing relationship: "
                f"{relationship.relationship_id}"
  )
