This project was run on windows. Type the following into the terminal to start:
```
python main.py
```

This project was not run on either Mac or Linux. But try the following in the terminal on those OSs:
```
python3 main.py
```

This project was only tested on Python 3.10.

This project aims to test out five different search algorithms on a maze with the following specifications:

### Maze specs:
- 1/3 of the maze spaces are obstacles
- multiple goal nodes
- random costs to enter each space

The goal is to see which search algorithms go towards which goal nodes and see if they choose similar goal nodes or completely different goal nodes. The performance of each algorithm will also be recorded. The performance is measured in the following way:

### Performance Measurements:
- number of nodes expanded
- max number of nodes in the open list (to-be-visited list)
- total cost of each path
- path length

Here are the search algorithms that will are under test:

### Search Algorithms:
- Breadth First Search
- Depth First Search
- Uniform Cost Search
- Greedy Best First Search
- A* Search

Once the program has finished running, the results of the run can be found in the "results" folder within the project.