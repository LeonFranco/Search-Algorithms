from typing import List
from maze.node import Node
from maze.nodetype import NodeType
from maze.maze import Maze

class Solver:
    maze: Maze
    openList: List[Node] = []
    numNodesExpanded: int = 0
    maxNumNodesInList: int = 0
    totalCost: int = 0
    path: List[Node] = []

    def __init__(self, maze) -> None:
        self.maze = maze

    def addToOpenList(self, node: Node):
        raise NotImplementedError("addToOpenList() not overriden")

    def takeFromOpenList(self):
        raise NotImplementedError("takeFromOpenList() not overriden")

    def solve(self):
        self.addToOpenList(self.maze.startNode)
        self.maxNumNodesInList = 1

        while True:
            currentNode = self.takeFromOpenList()

            if currentNode.type == NodeType.GOAL:
                self.totalCost = currentNode.g
                
                while currentNode is not None:
                    self.path.append(currentNode)
                    currentNode = currentNode.previousNode

                return

            if currentNode.isVisited: continue

            currentNode.isVisited = True
            self.numNodesExpanded += 1

            for neighbourNode in self.maze.getAdjacentNodes(currentNode):
                if neighbourNode.isVisited: continue

                neighbourNode.previousNode = currentNode
                neighbourNode.g += currentNode.g

                self.addToOpenList(neighbourNode)
            
            self.maxNumNodesInList = max(self.maxNumNodesInList, len(self.openList))

