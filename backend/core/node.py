"""Node model for the Nexus graph engine."""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Node:
    """Represent one entity in the digital identity graph."""

    id: str
    type: str
    properties: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.id.strip():
            raise ValueError("Node id cannot be empty.")
        if not self.type.strip():
            raise ValueError("Node type cannot be empty.")

    def to_dict(self) -> dict[str, Any]:
        """Serialize the node into a plain dictionary."""
        return {
            "id": self.id,
            "type": self.type,
            "properties": dict(self.properties),
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Node":
        """Create a node from a serialized dictionary."""
        return cls(
            id=str(data["id"]),
            type=str(data["type"]),
            properties=dict(data.get("properties", {})),
        )
