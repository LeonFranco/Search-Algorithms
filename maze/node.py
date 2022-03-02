from __future__ import annotations
from dataclasses import dataclass
from .nodetype import NodeType

@dataclass
class Node:
    type: NodeType = NodeType.PATH
    isVisited: bool = False
    row: int = -1
    col: int = -1
    g: int = 0
    h: int = -1
    previousNode: Node = None
