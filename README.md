Secrecy Mapper

«Evidence-driven entity resolution and structural network analysis.»

Status: Early development. The current implementation is focused on repository foundations and a tested analytical core using synthetic data. No production-readiness or real-world investigative accuracy is claimed.

Secrecy Mapper is an analytical system designed to transform heterogeneous records into structured, traceable entity-relationship networks.

Its purpose is to make complex ownership structures, intermediaries, connections and jurisdictional relationships easier to investigate and understand.

The project prioritises evidence provenance, entity resolution, relationship integrity, analytical reproducibility and explicit uncertainty.

---

1. Mission

Transform fragmented records into defensible analytical networks without losing the evidence and assumptions behind their construction.

Secrecy Mapper is designed around five principles:

1. Evidence before inference — analytical relationships must be traceable to supporting records.
2. Identity discipline — entities must not be merged without sufficient justification.
3. Relationship integrity — connections must preserve direction, type and supporting evidence.
4. Explicit uncertainty — confidence and unresolved identity questions must remain visible.
5. Reproducibility — analytical outputs must be repeatable and independently verifiable.

---

2. Analytical Scope

The system is intended to support analysis of:

- Individuals and organisations
- Corporate entities and ownership structures
- Jurisdictions
- Intermediaries
- Addresses and registered locations
- Directed and indirect relationships
- Entity-resolution candidates
- Network connectivity and structural position
- Evidence provenance and confidence

The analytical objective is not simply to produce a graph.

It is to establish a defensible representation of relationships between entities.

---

3. Core Analytical Architecture

The intended analytical workflow is:

Source Records → Validation → Entity Resolution → Relationship Construction → Graph Analysis → Findings → Evidence

Stage 1 — Source Records

Receive and preserve structured records from identifiable sources.

Stage 2 — Validation

Check record structure, required fields, identifiers and data integrity.

Stage 3 — Entity Resolution

Identify potential duplicate representations of the same real-world entity.

Uncertain matches must remain distinguishable from confirmed identities.

Stage 4 — Relationship Construction

Represent relationships using:

- Source entity
- Target entity
- Relationship type
- Supporting evidence
- Observation date
- Confidence assessment

Stage 5 — Graph Analysis

Construct directed networks and calculate structural measurements.

Stage 6 — Findings

Produce interpretable analytical outputs while distinguishing observations from assumptions and inferences.

Stage 7 — Evidence

Preserve the records and processing information required to reproduce and review analytical results.

---

4. Analytical Standards

Entity Integrity

Every entity should have a stable identifier.

Different records referring to potentially identical entities must not automatically be treated as the same entity.

Relationship Integrity

Every relationship should have:

- A unique relationship identifier
- A valid source entity
- A valid target entity
- A relationship type
- An evidence reference
- A confidence assessment
- An observation date

Evidence Provenance

Analytical relationships must retain traceability to their supporting records.

An inferred relationship must never be presented as a directly documented fact.

Network Interpretation

Metrics such as degree centrality, betweenness centrality and connectivity describe structural properties of a network.

They do not independently establish criminal conduct, misconduct or wrongdoing.

---

5. Technology Stack

Technology| Intended purpose
Python| Core analytical implementation
Pydantic| Structured record validation
Pandas| Tabular data processing
NetworkX| Graph construction and analysis
pytest| Automated testing
PyYAML| Configuration management
Git| Version control

Streamlit may be introduced later as an analytical interface.

The initial development priority is the underlying analytical engine.

---

6. Repository Structure

The planned architecture is:

Secrecy-Mapper/
│
├── README.md
├── SECURITY.md
├── .gitignore
├── .gitattributes
├── .env.example
├── pyproject.toml
├── requirements.txt
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│
├── src/
│   └── secrecy_mapper/
│       ├── __init__.py
│       ├── models.py
│       ├── validation.py
│       ├── entity_resolution.py
│       ├── relationships.py
│       ├── graph.py
│       ├── metrics.py
│       ├── uncertainty.py
│       └── pipeline.py
│
├── tests/
│
└── evidence/
    ├── validation/
    ├── network/
    └── manifests/

This represents the intended architecture. Components will be introduced and tested incrementally as development progresses.

---

7. Data Governance

Initial development and testing will use synthetic data.

Real-world records will only be introduced after appropriate consideration of:

- Source legitimacy
- Data provenance
- Privacy
- Legal access
- Data minimisation
- Storage and retention
- Analytical limitations

Raw records, processed datasets and generated analytical evidence must remain distinguishable.

Credentials and sensitive configuration must never be committed to version control.

See "SECURITY.md" (SECURITY.md).

---

8. Development Roadmap

Phase 1 — Repository Foundations

- Repository structure
- Python project configuration
- Dependency management
- Security policy
- Documentation

Phase 2 — Analytical Core

- Typed entity and relationship models
- Record validation
- Deterministic synthetic datasets
- Directed graph construction
- Structural network metrics
- Automated tests
- Reproducible analytical outputs

Phase 3 — Entity Resolution

- Candidate identification
- Attribute comparison
- Identity confidence
- Duplicate detection
- Resolution audit trail

Phase 4 — Evidence Architecture

- Evidence identifiers
- Source provenance
- Output manifests
- Hash verification
- Reproducibility checks

Phase 5 — Advanced Network Analysis

- Confidence-filtered networks
- Brokerage analysis
- Connectivity analysis
- Path analysis
- Uncertainty and sensitivity analysis

Phase 6 — Analytical Interface

- Network exploration
- Entity profiles
- Relationship inspection
- Evidence navigation
- Analytical reporting

---

9. Development Status

Current stage: Repository foundations and configuration.

The initial implementation will prioritise a functioning, tested analytical core using synthetic data.

The dashboard and advanced analytical capabilities will follow only after the underlying data and evidence architecture is established.

No production-readiness or real-world investigative accuracy is claimed at this stage.

---

10. Development

The project is being developed incrementally using synthetic data.

The initial analytical-core workflow is:

Source Records
      ↓
Validation
      ↓
Entity Resolution
      ↓
Relationship Construction
      ↓
Graph Analysis
      ↓
Findings
      ↓
Evidence Manifest

The analytical core must operate independently of Streamlit.

Once the package structure is implemented, install the development dependencies using:

python -m pip install -e ".[dev]"

Run the automated tests using:

pytest

The analytical interface will be introduced only after the underlying analytical outputs have been tested and their reproducibility established.

---

11. Governing Principle

A network is only as defensible as the evidence, identity decisions and assumptions used to construct it.

Secrecy Mapper is being developed to make those foundations visible, traceable and reproducible.
