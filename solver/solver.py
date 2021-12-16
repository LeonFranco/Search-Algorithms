from typing import List
from maze.node import Node
from maze.nodetype import NodeType
from maze.maze import Maze
import pprint

class Solver:
    def __init__(self, maze: Maze, algoName) -> None:
        self.maze = maze
        self.openList: List[Node] = list()
        self.numNodesExpanded: int = 0
        self.maxNumNodesInList: int = 0
        self.totalCost: int = 0
        self.path: List[Node] = list()
        self.pathLength: int = 0
        self.algoName = algoName

    def __str__(self) -> str:
        result = ""
        result += f"Nodes Expanded: {self.numNodesExpanded}\n"
        result += f"Max Nodes In Open List: {self.maxNumNodesInList}\n"
        result += f"Total Cost: {self.totalCost}\n"
        result += f"Path:\n"
        for node in self.path:
            result += f"    <{node.type}, Row: {node.row}, Column: {node.col}>\n"
        result += "\n" + self.maze.__str__()

        return result

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
                while currentNode is not None:
                    self.path.insert(0, currentNode)
                    self.totalCost += currentNode.g
                    currentNode = currentNode.previousNode
                self.pathLength = len(self.path)
                return

            if currentNode.isVisited: continue

            currentNode.isVisited = True
            self.numNodesExpanded += 1

            for neighbourNode in self.maze.getAdjacentNodes(currentNode):
                if neighbourNode.isVisited: continue

                neighbourNode.previousNode = currentNode

                self.addToOpenList(neighbourNode)
            
            self.maxNumNodesInList = max(self.maxNumNodesInList, len(self.openList))

    @staticmethod
    def calculateCurrentTotalCost(node: Node):
        totalCost = 0

        while node is not None:
            totalCost += node.g
            node = node.previousNode
        
        return totalCost