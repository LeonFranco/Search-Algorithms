from .solver import Solver
from maze.node import Node
import heapq
import random

class AStarSearchSolver(Solver):
    def __init__(self, maze) -> None:
        super().__init__(maze, "A* Search")

    def addToOpenList(self, node: Node):
        totalCost = self.calculateCurrentTotalCost(node)

        heapq.heappush(self.openList, (totalCost + node.h, random.random(), node))

    def takeFromOpenList(self):
        return heapq.heappop(self.openList)[~0]