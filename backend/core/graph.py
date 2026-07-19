"""Graph engine for Nexus."""

from backend.core.node import Node
from backend.core.relation import Relation


class Graph:
    """Store and manage nodes and relations."""

    def __init__(self) -> None:
        self.nodes: dict[str, Node] = {}
        self.relations: list[Relation] = []

    def add_node(self, node: Node) -> None:
        """Add a node and reject duplicate identifiers."""
        if node.id in self.nodes:
            raise ValueError(f"Node '{node.id}' already exists.")
        self.nodes[node.id] = node

    def get_node(self, node_id: str) -> Node | None:
        """Return a node by identifier, or None when absent."""
        return self.nodes.get(node_id)

    def node_exists(self, node_id: str) -> bool:
        """Return whether a node exists."""
        return node_id in self.nodes

    def add_relation(self, relation: Relation) -> None:
        """Add a relation only when both endpoint nodes exist."""
        if relation.source_id not in self.nodes:
            raise ValueError(
                f"Source node '{relation.source_id}' does not exist."
            )
        if relation.target_id not in self.nodes:
            raise ValueError(
                f"Target node '{relation.target_id}' does not exist."
            )
        self.relations.append(relation)
