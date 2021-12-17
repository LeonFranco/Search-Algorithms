import os
from maze.maze import Maze
from solver.solver import Solver

FOLDER_DIR = "results"

def getPath(fileName):
    return os.path.join(FOLDER_DIR, fileName)

def createResultFolder():
    if os.path.isdir(FOLDER_DIR): return

    os.makedirs(FOLDER_DIR)
    
def writeMaze(maze: Maze):
    path = getPath("maze.txt")

    legend = "S: Start\n" + "G: Goal\n" +  "#: Obstacle\n\n"

    with open(path, "w") as mazeFile:
        mazeFile.write(legend)
        mazeFile.write(maze.__str__())

def writeSolverStats(solver: Solver):
    modifiedName = solver.algoName.replace(" ", "-")
    path = getPath(f"{modifiedName}.txt")

    with open(path, "w") as solverFile:
        stats = formateSolverStates(solver)
        solverFile.write(stats)

def formateSolverStates(solver: Solver):
    return (f"{solver.algoName}\n\n"
            f"Number of nodes expaned: {solver.numNodesExpanded}\n"
            f"Max number of nodes in open list: {solver.maxNumNodesInList}\n"
            f"Total cost of final path: {solver.totalCost}\n"
            f"Path length: {len(solver.path)}\n"
            f"Start node: <row={solver.path[0].row}, col={solver.path[0].col}>\n"
            f"Goal node: <row={solver.path[~0].row}, col={solver.path[~0].col}>\n"
            f"Execution time: {solver.executionTime:.4f} sec\n")