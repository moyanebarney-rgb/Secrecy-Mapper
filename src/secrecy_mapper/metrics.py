import networkx as nx
import pandas as pd


def calculate_node_metrics(
    graph: nx.MultiDiGraph,
) -> pd.DataFrame:
    """Calculate structural metrics for every graph node."""

    betweenness = nx.betweenness_centrality(
        graph,
        normalized=True,
    )

    rows = []

    for node_id, attributes in graph.nodes(data=True):
        in_degree = graph.in_degree(node_id)
        out_degree = graph.out_degree(node_id)

        rows.append(
            {
                "entity_id": node_id,
                "name": attributes.get("name"),
                "entity_type": attributes.get("entity_type"),
                "in_degree": in_degree,
                "out_degree": out_degree,
                "total_degree": in_degree + out_degree,
                "betweenness_centrality": betweenness[node_id],
            }
        )

    return pd.DataFrame(rows)


def calculate_components(
    graph: nx.MultiDiGraph,
) -> list[list[str]]:
    """Identify weakly connected components."""

    components = [
        sorted(component)
        for component in nx.weakly_connected_components(graph)
    ]

    return sorted(
        components,
        key=lambda component: component[0],
  )
