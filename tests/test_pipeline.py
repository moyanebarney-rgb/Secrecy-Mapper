import json
from pathlib import Path

import pandas as pd

from secrecy_mapper.pipeline import run_pipeline


def test_pipeline_generates_expected_outputs():
    project_root = Path(__file__).resolve().parents[1]

    run_pipeline(project_root)

    output_dir = project_root / "evidence" / "network"

    metrics_file = output_dir / "node_metrics.csv"
    components_file = output_dir / "components.json"

    assert metrics_file.exists()
    assert components_file.exists()

    metrics = pd.read_csv(metrics_file)

    with open(components_file, encoding="utf-8") as file:
        components = json.load(file)

    assert len(metrics) == 7
    assert len(components) == 2

    intermediary = metrics.loc[
        metrics["entity_id"] == "X"
    ].iloc[0]

    assert intermediary["in_degree"] == 2
    assert intermediary["out_degree"] == 2
    assert intermediary["total_degree"] == 4
