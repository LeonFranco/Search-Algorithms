from maze.maze import Maze
from time import sleep
from pprint import PrettyPrinter
import copy
from solver.solver import Solver
from solver.depthfirstsearchsolver import DepthFirstSearchSolver

def main():
    # maze = Maze(45, 135) # * main
    maze = Maze()
    print(maze)
    depthSolver = DepthFirstSearchSolver(copy.deepcopy(maze))
    depthSolver.solve()
    print(depthSolver)

if __name__ == "__main__":
    main()