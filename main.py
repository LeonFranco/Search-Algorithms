from maze.maze import Maze
from driver import Driver
import time

def main():
    print("=== Program - Start ===")
    timer = time.perf_counter()

    driver = Driver(Maze(rowLength=1100, columnLength=1100))
    driver.start()

    timer = time.perf_counter() - timer
    print(f"=== Program - Finish (Execution time: {(timer / 60):.4f} min) ===")

if __name__ == "__main__": main()