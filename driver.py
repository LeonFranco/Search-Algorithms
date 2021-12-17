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
        self.maze: Maze = maze
        self.solvers: List[Solver] = []

    def start(self):
        self.initializatSolvers()
        self.executeSolvers()

    def initializatSolvers(self):
        print("Initialize solvers - Start")
        timer = time.perf_counter()

        solverClasses = [
            DepthFirstSearchSolver,
            BreadthFirstSearchSolver,
            UniformCostSearchSolver,
            GreedyBestFirstSearch,
            AStarSearchSolver,
        ]

        threads: List[threading.Thread] = []
        solverListLock = threading.Lock()

        for solverClass in solverClasses:
            def worker():
                solver: Solver = solverClass(copy.deepcopy(self.maze))
                with solverListLock:
                    self.solvers.append(solver)

            thread = threading.Thread(target=worker)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

        timer = time.perf_counter() - timer
        print(f"Initialize solvers - Finish (Execution time: {timer:.4f} sec)")

    def executeSolvers(self):
        print("Execute all solvers - Start")
        timer = time.perf_counter()

        threads: List[threading.Thread] = []

        for solver in self.solvers:
            thread = threading.Thread(target=solver.solve)
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()
        
        timer = time.perf_counter() - timer
        print(f"Execute all solvers - Finish (Execution time: {timer:.4f} sec)")

    def getResults(self):
        result.createResultFolder()
        result.writeMaze(self.maze)

        for solver in self.solvers:
            result.writeSolverStats(solver)
