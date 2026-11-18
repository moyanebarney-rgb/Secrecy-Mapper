import networkx as nx

from secrecy_mapper.graph import build_graph
from secrecy_mapper.metrics import (
    calculate_components,
    calculate_node_metrics,
)
from secrecy_mapper.models import Entity, Relationship


def test_graph_is_directed_multigraph():
    entities = [
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

    relationships = [
        Relationship(
            relationship_id="R001",
            source_id="A",
            target_id="B",
            relationship_type="ownership",
            evidence_id="E001",
            confidence="high",
            observed_at="2026-01-15",
        )
    ]

    graph = build_graph(entities, relationships)

    assert isinstance(graph, nx.MultiDiGraph)
    assert graph.number_of_nodes() == 2
    assert graph.number_of_edges() == 1


def test_evidence_is_preserved():
    entities = [
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

    relationships = [
        Relationship(
            relationship_id="R001",
            source_id="A",
            target_id="B",
            relationship_type="ownership",
            evidence_id="E001",
            confidence="high",
            observed_at="2026-01-15",
        )
    ]

    graph = build_graph(entities, relationships)

    edge = graph["A"]["B"]["R001"]

    assert edge["relationship_id"] == "R001"
    assert edge["evidence_id"] == "E001"
    assert edge["relationship_type"] == "ownership"
    assert edge["confidence"] == "high"
    assert edge["observed_at"] == "2026-01-15"


def test_multiple_relationships_between_same_entities_are_preserved():
    entities = [
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

    relationships = [
        Relationship(
            relationship_id="R001",
            source_id="A",
            target_id="B",
            relationship_type="ownership",
            evidence_id="E001",
            confidence="high",
            observed_at="2026-01-15",
        ),
        Relationship(
            relationship_id="R002",
            source_id="A",
            target_id="B",
            relationship_type="investment",
            evidence_id="E002",
            confidence="medium",
            observed_at="2026-02-15",
        ),
    ]

    graph = build_graph(entities, relationships)

    assert graph.number_of_edges() == 2
    assert "R001" in graph["A"]["B"]
    assert "R002" in graph["A"]["B"]


def test_metrics_and_components():
    entities = [
        Entity(entity_id="A", entity_type="organisation", name="A"),
        Entity(entity_id="B", entity_type="organisation", name="B"),
        Entity(entity_id="X", entity_type="organisation", name="X"),
        Entity(entity_id="E", entity_type="organisation", name="E"),
    ]

    relationships = [
        Relationship(
            relationship_id="R001",
            source_id="A",
            target_id="X",
            relationship_type="ownership",
            evidence_id="E001",
            confidence="high",
            observed_at="2026-01-15",
        ),
        Relationship(
            relationship_id="R002",
            source_id="X",
            target_id="B",
            relationship_type="ownership",
            evidence_id="E002",
            confidence="medium",
            observed_at="2026-01-16",
        ),
    ]

    graph = build_graph(entities, relationships)

    metrics = calculate_node_metrics(graph)
    components = calculate_components(graph)

    intermediary = metrics.loc[
        metrics["entity_id"] == "X"
    ].iloc[0]

    assert intermediary["in_degree"] == 1
    assert intermediary["out_degree"] == 1
    assert intermediary["total_degree"] == 2

    assert len(components) == 2
