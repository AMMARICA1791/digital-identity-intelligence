"""Tests for the Nexus Node model."""

import unittest

from backend.core.node import Node


class NodeTestCase(unittest.TestCase):
    def test_node_round_trip(self) -> None:
        node = Node(
            id="github-account-1",
            type="account",
            properties={"platform": "GitHub"},
        )

        restored = Node.from_dict(node.to_dict())

        self.assertEqual(restored, node)

    def test_empty_id_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            Node(id=" ", type="account")


if __name__ == "__main__":
    unittest.main()
