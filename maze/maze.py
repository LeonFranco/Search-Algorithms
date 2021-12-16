from .node import Node
from .nodetype import NodeType
from typing import List
import globalconstants
import random
import math
from collections import deque
import copy
import heapq

random.seed(globalconstants.SEED)

class Maze:
    def __init__(self, rowLength=10, columnLength=10) -> None:
        if  rowLength < 10 or columnLength < 10:
            raise ValueError("rowLength and columnLength must both be at least 10")

        print("Start maze creation")

        self.rowLength: int = rowLength
        self.columnLength: int = columnLength
        self.maze: List[Node] = []
        self.startNode: Node = None
        self.goalNodes: List[Node] = []

        self.generateMazeTemplate()
        self.selectStartNode()
        self.selectGoalNodes()
        self.calculateHeuristics()
        self.addObstacles()
        self.generateRandomCosts()

        print("Finish maze creation")

    def __str__(self) -> str:
        result = ""

        for row in range(self.rowLength + 2):
            result += ""

            for col in range(self.columnLength + 2):
                node = self.maze[row][col]
                match node.type:
                    case NodeType.OBSTACLE:
                        result += "# "
                    case NodeType.PATH:
                        if node.isVisited: result += "* "
                        else:              result += "  "
                    case NodeType.START:
                        result += "S "
                    case NodeType.GOAL:
                        result += "G "
            result += "\n"

        return result

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
        row = self.rowLength // 2
        col = self.columnLength // 2

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
        proportionAsObstacles = 0.33
        totalNumberNodes = self.rowLength * self.columnLength
        numOfObstacleNodes = totalNumberNodes * proportionAsObstacles
        obstacleGenerateCounter = 0
        
        currentObstacles = []
        mazeCopy = sum(copy.copy(self.maze), [])
        random.shuffle(mazeCopy)

        while proportionAsObstacles > 0.0:
            while obstacleGenerateCounter < numOfObstacleNodes:
                node = mazeCopy.pop(0)

                if node.type != NodeType.PATH:
                    mazeCopy.append(node)
                    continue

                node.type = NodeType.OBSTACLE
                currentObstacles.append(node)
                obstacleGenerateCounter += 1

                mazeCopy.append(node)
            
            if self.isValidMaze(): break

            for node in currentObstacles:
                node.type = NodeType.PATH
            currentObstacles.clear()
            
            obstacleGenerateCounter = 0
            proportionAsObstacles -= 0.01
            numOfObstacleNodes = totalNumberNodes * proportionAsObstacles

    def isValidMaze(self):
        visited = list()
        toBeVisited = list()
        heapq.heappush(toBeVisited, (self.startNode.h, random.random(), self.startNode))

        isValid = False

        while toBeVisited:
            currentNode = heapq.heappop(toBeVisited)[~0]

            if currentNode.isVisited: continue

            currentNode.isVisited = True
            visited.append(currentNode)

            if currentNode.type == NodeType.GOAL and all(node.isVisited for node in self.goalNodes):
                isValid = True
                break

            for node in self.getAdjacentNodes(currentNode):
                heapq.heappush(toBeVisited, (node.h, random.random(), node))

        self.resetVisitedNodes(visited)
        return isValid
            
    def getAdjacentNodes(self, node: Node):
        neighbourNodeCoordinates = [
            (node.row - 1, node.col), # up
            # (node.row - 1, node.col + 1), # up + right
            (node.row, node.col + 1), # right
            # (node.row + 1, node.col + 1), # down + right
            (node.row + 1, node.col), # down
            # (node.row + 1, node.col - 1), # down + left
            (node.row, node.col - 1),  # left
            # (node.row - 1, node.col - 1) # up + left
        ]

        neighbourNodes = []

        for (row, col) in neighbourNodeCoordinates:
            currentNode = self.maze[row][col]

            if currentNode.type == NodeType.OBSTACLE: continue

            neighbourNodes.append(currentNode)

        return neighbourNodes

    def resetVisitedNodes(self, visited: List[Node]):
        for node in visited:
            node.isVisited = False

    def generateRandomCosts(self):
        MIN_COST = 1
        MAX_COST = 5

        for row in self.maze:
            for node in row:
                if node.type == NodeType.OBSTACLE or node.type == NodeType.START: continue
                node.g = random.randint(MIN_COST, MAX_COST)

    # heuristic is straight line distance to the NEAREST goal
    # straight line distance is used instead of Manhattan Distance since diagonal movement is allowed
    def calculateHeuristics(self):
        for row in self.maze:
            for node in row:
                if node.type == NodeType.OBSTACLE or node.type == NodeType.GOAL: continue
                node.h = min(self.calculateManhattanDistance(node, goal) for goal in self.goalNodes)

    @staticmethod
    def calculateManhattanDistance(node1: Node, node2: Node):
        return abs(node1.row - node2.row) + abs(node1.col - node2.col)

    @staticmethod
    def calculateStraightLineDistance(node1: Node, node2: Node):
        return math.sqrt((node1.row - node2.row) ** 2 + (node1.col - node2.col) ** 2)
