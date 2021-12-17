from typing import List
from maze.maze import Maze
from time import sleep
from pprint import PrettyPrinter
import copy
from solver.solver import Solver
from solver.depthfirstsearchsolver import DepthFirstSearchSolver
from solver.breadthfirstsearchsolver import BreadthFirstSearchSolver
from solver.uniformcostsearchsolver import UniformCostSearchSolver
from solver.greedybestfirstsearchsolver import GreedyBestFirstSearch
from solver.astarsearchsolver import AStarSearchSolver
import result
from driver import Driver

def main():
    driver = Driver(Maze(1000, 1000))
    driver.start()
    driver.getResults()

if __name__ == "__main__": main()