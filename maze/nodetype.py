import enum
from enum import Enum

class NodeType(Enum):
    PATH = enum.auto()
    OBSTACLE = enum.auto()
    START = enum.auto()
    GOAL = enum.auto()