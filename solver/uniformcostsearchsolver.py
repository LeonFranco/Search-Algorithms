from .solver import Solver
from maze.node import Node
import heapq
import random

class UniformCostSearchSolver(Solver):
    def __init__(self, maze) -> None:
        super().__init__(maze)

    def addToOpenList(self, node: Node):
        heapq.heappush(self.openList, (node.g, random.random(),node))

    def takeFromOpenList(self):
        return heapq.heappop(self.openList)[~0]