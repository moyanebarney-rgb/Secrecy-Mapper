import json
import shutil
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal

from secrecy_mapper.pipeline import run_pipeline


def test_pipeline_generates_expected_outputs(tmp_path: Path):
    """Verify pipeline outputs against the published evidence."""

    # Locate the repository.
    source_root = Path(__file__).resolve().parents[1]

    # Create an isolated temporary project.
    project_root = tmp_path / "secrecy_mapper_test"

    data_dir = project_root / "data" / "synthetic"
    data_dir.mkdir(parents=True)

    # Copy synthetic source datasets into the temporary project.
    for name in ("entities.csv", "relationships.csv"):
        shutil.copy(
            source_root / "data" / "synthetic" / name,
            data_dir / name,
        )

    # Execute the pipeline in the temporary project.
    run_pipeline(project_root)

    # Locate generated outputs.
    output_dir = project_root / "evidence" / "network"

    metrics_file = output_dir / "node_metrics.csv"
    components_file = output_dir / "components.json"

    assert metrics_file.exists()
    assert components_file.exists()

    # Read generated outputs.
    generated_metrics = pd.read_csv(metrics_file)

    with open(components_file, encoding="utf-8") as file:
        generated_components = json.load(file)

    # Locate published reference evidence.
    reference_dir = source_root / "evidence" / "network"

    reference_metrics_file = reference_dir / "node_metrics.csv"
    reference_components_file = reference_dir / "components.json"

    assert reference_metrics_file.exists()
    assert reference_components_file.exists()

    # Read published reference evidence.
    reference_metrics = pd.read_csv(reference_metrics_file)

    with open(reference_components_file, encoding="utf-8") as file:
        reference_components = json.load(file)

    # Verify generated evidence matches published evidence.
    assert_frame_equal(
        generated_metrics,
        reference_metrics,
        check_dtype=True,
    )

    assert generated_components == reference_components

    # Verify expected network structure.
    assert len(generated_metrics) == 7
    assert len(generated_components) == 2

    # Verify intermediary network metrics.
    intermediary = generated_metrics.loc[
        generated_metrics["entity_id"] == "X"
    ].iloc[0]

    assert intermediary["in_degree"] == 2
    assert intermediary["out_degree"] == 2
    assert intermediary["total_degree"] == 4 
