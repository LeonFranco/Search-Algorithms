from .solver import Solver
from maze.node import Node

class BreadthFirstSearchSolver(Solver):
    def __init__(self, maze) -> None:
        super().__init__(maze, "Breadth First Search")

    def addToOpenList(self, node: Node):
        self.openList.append(node)

    def takeFromOpenList(self):
        return self.openList.pop(0)