from maze.maze import Maze
from time import sleep
from pprint import PrettyPrinter
import copy

def main():
    maze1 = Maze(45, 135)
    maze2 = copy.deepcopy(maze1)

    assert(maze1.maze is not maze2.maze), "Same maze"

    for row in range(maze1.rowLength):
        for col in range(maze2.columnLength):
            assert(maze1.maze[row][col] is not maze2.maze[row][col]), "Same node"
    
    assert(maze1.startNode is not maze2.startNode), "Same start node"

    assert(maze1.goalNodes is not maze2.goalNodes), "Same goal nodes"

    for i in range(len(maze1.goalNodes)):
        assert(maze1.goalNodes[i] is not maze2.goalNodes[i]), "Same goal node"

    print(maze2.maze[0][0])

if __name__ == "__main__":
    main()