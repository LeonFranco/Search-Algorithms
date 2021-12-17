from maze.maze import Maze
from driver import Driver

def main():
    driver = Driver(Maze(rowLength=1100, columnLength=1100))
    driver.start()
    driver.getResults()

if __name__ == "__main__": main()