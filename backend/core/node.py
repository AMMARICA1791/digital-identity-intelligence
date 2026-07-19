from dataclasses import dataclass, field
from typing import Any


@dataclass
class Node:
    id: str
        type: str
            properties: dict[str, Any] = field(default_factory=dict)

                def to_dict(self) -> dict[str, Any]:
                        return {
                                    "id": self.id,
                                                "type": self.type,
                                                            "properties": self.properties,
                                                                    }