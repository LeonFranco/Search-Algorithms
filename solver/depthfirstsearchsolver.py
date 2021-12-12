from .solver import Solver
from maze.node import Node

class DepthFirstSearchSolver(Solver):
    def __init__(self, maze) -> None:
        super().__init__(maze)

    def addToOpenList(self, node: Node):
        self.openList.append(node)

    def takeFromOpenList(self):
        return self.openList.pop()