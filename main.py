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

def main():
    maze = Maze(500, 500) # * main
    # maze = Maze()
    result.createResultFolder()
    result.writeMaze(maze)


    # print(maze)
    solvers: List[Solver] = [
        DepthFirstSearchSolver(copy.deepcopy(maze)),
        # BreadthFirstSearchSolver(copy.deepcopy(maze)),
        # UniformCostSearchSolver(copy.deepcopy(maze)),
        # GreedyBestFirstSearch(copy.deepcopy(maze)),
        # AStarSearchSolver(copy.deepcopy(maze)),
    ]

    for solver in solvers:
        solver.solve()
        result.writeSolverStats(solver)

if __name__ == "__main__": main()