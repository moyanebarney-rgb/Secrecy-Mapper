import networkx as nx

from secrecy_mapper.models import Entity, Relationship
from secrecy_mapper.validation import validate_dataset


def build_graph(
    entities: list[Entity],
    relationships: list[Relationship],
) -> nx.MultiDiGraph:
    """Build an evidence-preserving directed graph."""

    validate_dataset(entities, relationships)

    graph = nx.MultiDiGraph()

    for entity in entities:
        graph.add_node(
            entity.entity_id,
            entity_type=entity.entity_type,
            name=entity.name,
        )

    for relationship in relationships:
        graph.add_edge(
            relationship.source_id,
            relationship.target_id,
            key=relationship.relationship_id,
            relationship_id=relationship.relationship_id,
            relationship_type=relationship.relationship_type,
            evidence_id=relationship.evidence_id,
            confidence=relationship.confidence,
            observed_at=relationship.observed_at.isoformat(),
        )

    return graph
