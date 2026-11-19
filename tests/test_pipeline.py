import json
import shutil
from pathlib import Path

import pandas as pd

from secrecy_mapper.pipeline import run_pipeline


def test_pipeline_generates_expected_outputs(tmp_path: Path):
    source_root = Path(__file__).resolve().parents[1]
    project_root = tmp_path / "secrecy_mapper_test"

    data_dir = project_root / "data" / "synthetic"
    data_dir.mkdir(parents=True)

    for name in ("entities.csv", "relationships.csv"):
        shutil.copy(source_root / "data" / "synthetic" / name, data_dir / name)

    run_pipeline(project_root)

    output_dir = project_root / "evidence" / "network"
    metrics_file = output_dir / "node_metrics.csv"
    components_file = output_dir / "components.json"

    assert metrics_file.exists()
    assert components_file.exists()

    metrics = pd.read_csv(metrics_file)
    with open(components_file, encoding="utf-8") as f:
        components = json.load(f)

    assert len(metrics) == 7
    assert len(components) == 2

    x = metrics.loc[metrics["entity_id"] == "X"].iloc[0]
    assert x["in_degree"] == 2
    assert x["out_degree"] == 2
    assert x["total_degree"] == 4
