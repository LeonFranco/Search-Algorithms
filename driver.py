from typing import List
from maze.maze import Maze
from solver.solver import Solver
from solver.depthfirstsearchsolver import DepthFirstSearchSolver
from solver.breadthfirstsearchsolver import BreadthFirstSearchSolver
from solver.uniformcostsearchsolver import UniformCostSearchSolver
from solver.greedybestfirstsearchsolver import GreedyBestFirstSearch
from solver.astarsearchsolver import AStarSearchSolver
import multiprocessing
import result
import time

class Driver:
    def __init__(self, maze: Maze) -> None:
        self.maze: Maze = maze

    def start(self):
        result.createResultFolder()
        result.writeMaze(self.maze)

        print("Execute all solvers - Start")
        timer = time.perf_counter()

        solverClasses = [
            DepthFirstSearchSolver,
            BreadthFirstSearchSolver,
            UniformCostSearchSolver,
            GreedyBestFirstSearch,
            AStarSearchSolver,
        ]

        processes: List[multiprocessing.Process] = []

        for solverClass in solverClasses:
            process = multiprocessing.Process(target=self.worker, args=[solverClass(self.maze)])
            process.start()
            processes.append(process)

        for process in processes:
            process.join()

        timer = time.perf_counter() - timer
        print(f"Execute all solvers - Finish (Execution time: {timer:.4f} sec)")

    def getResults(self):
        result.createResultFolder()
        result.writeMaze(self.maze)

        for solver in self.solvers:
            result.writeSolverStats(solver)

    def worker(self, solver):
        solver.solve()
        import result
        result.writeSolverStats(solver)
