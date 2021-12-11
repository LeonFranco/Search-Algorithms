from .node import Node
from .nodetype import NodeType
from typing import List
import globalconstants
import random
import math
from collections import deque
import copy

random.seed(globalconstants.SEED)

class Maze:
    rowLength: int
    columnLength: int
    maze: List[Node] = []
    startNode: Node
    goalNodes: List[Node] = []

    def __init__(self, rowLength=10, columnLength=10) -> None:
        if  rowLength < 10 or columnLength < 10:
            raise ValueError("rowLength and columnLength must both be at least 10")

        self.rowLength = rowLength
        self.columnLength = columnLength

        self.generateMazeTemplate()
        self.selectStartNode()
        self.selectGoalNodes()
        self.addObstacles()
        self.generateRandomCosts()
        self.calculateHeuristics()

    def __str__(self) -> str:
        result = ""

        for row in range(self.rowLength + 2):
            for col in range(self.columnLength + 2):
                node = self.maze[row][col]
                match node.type:
                    case NodeType.OBSTACLE:
                        result += "# "
                    case NodeType.PATH:
                        result += ". "
                    case NodeType.START:
                        result += "S "
                    case NodeType.GOAL:
                        result += "G "
            result += "\n"

        return result

    def generateMazeTemplate(self) -> None:
        obstacleNodeList = [Node(type=NodeType.OBSTACLE)]

        self.maze.append(obstacleNodeList + obstacleNodeList * self.columnLength + obstacleNodeList)

        for row in range(self.rowLength):
            currentRow = []
            currentRow += obstacleNodeList

            for col in range(self.columnLength):
                currentRow.append(Node(row=row+1, col=col+1))

            currentRow += obstacleNodeList
            self.maze.append(currentRow)

        self.maze.append(obstacleNodeList + obstacleNodeList * self.columnLength + obstacleNodeList)

    def selectStartNode(self):
        row = random.randint(1, self.rowLength)
        col = random.randint(1, self.columnLength)

        node = self.maze[row][col]

        node.type = NodeType.START
        self.startNode = node

    def selectGoalNodes(self):
        if self.rowLength == self.columnLength:
            numOfGoalNodes = self.rowLength
        else:
            numOfGoalNodes = math.sqrt(self.rowLength * self.columnLength)
        numOfGoalNodes = int(math.sqrt(numOfGoalNodes))

        goalGenerateCounter = 0

        while goalGenerateCounter != numOfGoalNodes:
            row = random.randint(1, self.rowLength)
            col = random.randint(1, self.columnLength)
            
            node = self.maze[row][col]

            if node.type != NodeType.PATH: continue

            node.type = NodeType.GOAL
            self.goalNodes.append(node)

            goalGenerateCounter += 1

    def addObstacles(self):
        numOfObstacleNodes = len(self.goalNodes) * 4
        obstacleGenerateCounter = 0

        while obstacleGenerateCounter != numOfObstacleNodes:
            row = random.randint(1, self.rowLength)
            col = random.randint(1, self.columnLength)
            
            node = self.maze[row][col]

            if node.type != NodeType.PATH: continue

            node.type = NodeType.OBSTACLE

            if (self.isValidMaze()):
                obstacleGenerateCounter += 1
                continue

            node.type = NodeType.PATH

    def isValidMaze(self):
        toBeVisited = deque()
        toBeVisited.append(self.startNode)

        isValid = False

        while toBeVisited:
            currentNode = toBeVisited.pop()

            if currentNode.isVisited: continue

            currentNode.isVisited = True

            if currentNode.type == NodeType.GOAL and all(node.isVisited for node in self.goalNodes):
                isValid = True
                break

            for node in self.getAdjacentNodes(currentNode):
                toBeVisited.append(node)

        self.resetVisitedNodes()
        return isValid
            
    def getAdjacentNodes(self, node: Node):
        neighbourNodeCoordinates = [
            (node.row + 1, node.col), # up
            (node.row, node.col + 1), # right
            (node.row - 1, node.col), # down
            (node.row, node.col - 1)  # left
        ]

        neighbourNodes = []

        for (row, col) in neighbourNodeCoordinates:
            currentNode = self.maze[row][col]

            if currentNode.type == NodeType.OBSTACLE: continue

            neighbourNodes.append(currentNode)

        return neighbourNodes

    def resetVisitedNodes(self):
        for row in self.maze:
            for node in row:
                node.isVisited = False

    def generateRandomCosts(self):
        MIN_COST = 1
        MAX_COST = 100

        for row in self.maze:
            for node in row:
                if node.type == NodeType.OBSTACLE or node.type == NodeType.START: continue
                node.g = random.randint(MIN_COST, MAX_COST)

    def calculateHeuristics(self):
        for row in self.maze:
            for node in row:
                if node.type == NodeType.OBSTACLE or node.type == NodeType.GOAL: continue
                node.h = min(self.calculateManhattanDistance(node, goal) for goal in self.goalNodes)

    def __deepcopy__(self, memo):
        cls = self.__class__
        result = cls.__new__(cls)
        memo[id(self)] = result

        result.rowLength = self.rowLength
        result.columnLength = self.columnLength
        result.maze = copy.deepcopy(self.maze, memo)
        result.startNode = result.maze[self.startNode.row][self.startNode.col]
        result.goalNodes = [result.maze[node.row][node.col] for node in self.goalNodes]

        return result

    @staticmethod
    def calculateManhattanDistance(node1: Node, node2: Node):
        return abs(node1.row - node2.row) + abs(node1.col - node2.col)