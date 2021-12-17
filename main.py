from maze.maze import Maze
from driver import Driver

def main():
    driver = Driver(Maze(rowLength=1000, columnLength=1000))
    driver.start()

if __name__ == "__main__": main()