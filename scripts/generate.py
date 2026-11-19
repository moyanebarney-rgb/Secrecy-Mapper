from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]

DATA_DIR = ROOT / "data" / "synthetic"

DATA_DIR.mkdir(parents=True, exist_ok=True)


entities = [
    {
        "entity_id": "A",
        "entity_type": "organisation",
        "name": "Alpha Holdings",
    },
    {
        "entity_id": "B",
        "entity_type": "organisation",
        "name": "Beta Trading",
    },
    {
        "entity_id": "C",
        "entity_type": "organisation",
        "name": "Central Investments",
    },
    {
        "entity_id": "D",
        "entity_type": "organisation",
        "name": "Delta Services",
    },
    {
        "entity_id": "E",
        "entity_type": "organisation",
        "name": "Echo Capital",
    },
    {
        "entity_id": "F",
        "entity_type": "organisation",
        "name": "Foxtrot Logistics",
    },
    {
        "entity_id": "X",
        "entity_type": "organisation",
        "name": "Intermediary Group",
    },
]


relationships = [
    {
        "relationship_id": "R001",
        "source_id": "A",
        "target_id": "X",
        "relationship_type": "ownership",
        "evidence_id": "E001",
        "confidence": "high",
        "observed_at": "2026-01-15",
    },
    {
        "relationship_id": "R002",
        "source_id": "C",
        "target_id": "X",
        "relationship_type": "ownership",
        "evidence_id": "E002",
        "confidence": "medium",
        "observed_at": "2026-02-10",
    },
    {
        "relationship_id": "R003",
        "source_id": "X",
        "target_id": "B",
        "relationship_type": "control",
        "evidence_id": "E003",
        "confidence": "medium",
        "observed_at": "2026-02-18",
    },
    {
        "relationship_id": "R004",
        "source_id": "X",
        "target_id": "D",
        "relationship_type": "ownership",
        "evidence_id": "E004",
        "confidence": "low",
        "observed_at": "2026-03-05",
    },
    {
        "relationship_id": "R005",
        "source_id": "E",
        "target_id": "F",
        "relationship_type": "investment",
        "evidence_id": "E005",
        "confidence": "high",
        "observed_at": "2026-03-12",
    },
]


pd.DataFrame(entities).to_csv(
    DATA_DIR / "entities.csv",
    index=False,
)

pd.DataFrame(relationships).to_csv(
    DATA_DIR / "relationships.csv",
    index=False,
)

print("Synthetic dataset generated.")
print(f"Entities: {len(entities)}")
print(f"Relationships: {len(relationships)}")
