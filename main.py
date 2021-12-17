from maze.maze import Maze
from driver import Driver
import time

def main():
    print("=== Program - Start ===")
    timer = time.perf_counter()

    driver = Driver(Maze(rowLength=2000, columnLength=2000))
    driver.start()

    timer = time.perf_counter() - timer
    print(f"=== Program - Finish (Execution time: {timer:.4f} sec) ===")

if __name__ == "__main__": main()