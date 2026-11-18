import json
from pathlib import Path

import pandas as pd

from secrecy_mapper.graph import build_graph
from secrecy_mapper.metrics import (
    calculate_components,
    calculate_node_metrics,
)
from secrecy_mapper.models import Entity, Relationship


def run_pipeline(
    project_root: Path | None = None,
) -> None:
    """Execute the Secrecy Mapper analytical pipeline."""

    if project_root is None:
        project_root = Path(__file__).resolve().parents[2]

    data_dir = project_root / "data" / "synthetic"
    evidence_dir = project_root / "evidence" / "network"

    evidence_dir.mkdir(parents=True, exist_ok=True)

    entity_records = pd.read_csv(
        data_dir / "entities.csv"
    ).to_dict(orient="records")

    relationship_records = pd.read_csv(
        data_dir / "relationships.csv"
    ).to_dict(orient="records")

    entities = [
        Entity.model_validate(record)
        for record in entity_records
    ]

    relationships = [
        Relationship.model_validate(record)
        for record in relationship_records
    ]

    graph = build_graph(entities, relationships)

    metrics = calculate_node_metrics(graph)

    components = calculate_components(graph)

    metrics.to_csv(
        evidence_dir / "node_metrics.csv",
        index=False,
    )

    with open(
        evidence_dir / "components.json",
        "w",
        encoding="utf-8",
    ) as file:
        json.dump(
            components,
            file,
            indent=4,
        )

    print("Secrecy Mapper pipeline completed.")
    print(f"Entities: {graph.number_of_nodes()}")
    print(f"Relationships: {graph.number_of_edges()}")
    print(f"Components: {len(components)}")


if __name__ == "__main__":
    run_pipeline()
