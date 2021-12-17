from maze.maze import Maze
from driver import Driver

def main():
    driver = Driver(Maze(rowLength=2000, columnLength=2000))
    driver.start()
    driver.getResults()

if __name__ == "__main__": main()