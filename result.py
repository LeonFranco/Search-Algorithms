import os
from maze.maze import Maze

FOLDER_DIR = "results"

def createResultFolder():
    if os.path.isdir(FOLDER_DIR): return

    os.makedirs(FOLDER_DIR)
    
def writeMaze(maze: Maze):
    path = os.path.join(FOLDER_DIR, "maze.txt")

    legend = "S: Start\n" + "G: Goal\n" +  "#: Obstacle\n\n"

    with open(path, "w") as mazeFile:
        mazeFile.write(legend)
        mazeFile.write(maze.__str__())