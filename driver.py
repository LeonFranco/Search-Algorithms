from typing import List
from maze.maze import Maze
from solver.solver import Solver
from solver.depthfirstsearchsolver import DepthFirstSearchSolver
from solver.breadthfirstsearchsolver import BreadthFirstSearchSolver
from solver.uniformcostsearchsolver import UniformCostSearchSolver
from solver.greedybestfirstsearchsolver import GreedyBestFirstSearch
from solver.astarsearchsolver import AStarSearchSolver
import copy
import threading
import result
import time

class Driver:
    def __init__(self, maze: Maze) -> None:
        print("Program driver initialization - Start")
        timer = time.perf_counter()

        self.maze = maze
        self.solvers: List[Solver] = [
            DepthFirstSearchSolver(copy.deepcopy(self.maze)),
            BreadthFirstSearchSolver(copy.deepcopy(self.maze)),
            UniformCostSearchSolver(copy.deepcopy(self.maze)),
            GreedyBestFirstSearch(copy.deepcopy(self.maze)),
            AStarSearchSolver(copy.deepcopy(self.maze)),
        ]

        timer = time.perf_counter() - timer
        print(f"Program driver initialization - Finish (Execution time: {timer:.4f} sec)")

    def start(self):
        print("All solvers - Start")
        timer = time.perf_counter()

        threads: List[threading.Thread] = []

        for solver in self.solvers:
            thread = threading.Thread(target=solver.solve)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        
        timer = time.perf_counter() - timer
        print(f"All solvers - Finish (Execution time: {timer:.4f} sec)")

    def getResults(self):
        result.createResultFolder()
        result.writeMaze(self.maze)

        for solver in self.solvers:
            result.writeSolverStats(solver)

solvers = [DepthFirstSearchSolver]
