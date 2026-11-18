from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Entity(BaseModel):
    """A canonical entity represented in the analytical system."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    entity_id: str = Field(min_length=1)
    entity_type: str = Field(min_length=1)
    name: str = Field(min_length=1)


class Relationship(BaseModel):
    """A directed relationship between two entities."""

    model_config = ConfigDict(
        extra="forbid",
        str_strip_whitespace=True,
    )

    relationship_id: str = Field(min_length=1)
    source_id: str = Field(min_length=1)
    target_id: str = Field(min_length=1)
    relationship_type: str = Field(min_length=1)
    evidence_id: str = Field(min_length=1)

    confidence: Literal["low", "medium", "high"]

    observed_at: date
