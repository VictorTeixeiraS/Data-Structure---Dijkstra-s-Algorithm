# Dijkstra's Algorithm

This Python program demonstrates the implementation of Dijkstra's algorithm to find the shortest path in a graph. It utilizes the `heapq` library for efficient priority queue operations.

## Dijkstra's Algorithm

[Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm) is a popular graph traversal algorithm used to find the shortest path between two vertices in a weighted graph. It works by iteratively expanding the search from the starting vertex and updating the distances to other vertices as it explores the graph. The algorithm maintains a priority queue of vertices, prioritizing them based on their current shortest distance from the start vertex.

## The `heapq` Library

The `heapq` library is a built-in Python module that provides an implementation of the heap queue algorithm. In this program, it is used to create a priority queue for efficient selection of vertices with the minimum distance during the execution of Dijkstra's algorithm. The `heapq` module provides functions to push items onto the queue (`heapq.heappush`) and pop the smallest item from the queue (`heapq.heappop`).

## Usage

1. Install the required dependencies:
   - `pip install heapq` (no installation needed for the built-in `heapq` module)

2. Run the program:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the Python file.
   - Execute the command: `python mapa.py`

3. Follow the on-screen instructions:
   - Enter the choice '1' to find the shortest path.
   - Enter the starting vertex and the destination vertex.
   - The program will display the shortest path and the shortest distance between the vertices.

4. Exit the program:
   - Enter the choice '2' to exit the program.

## Contributing

Contributions to this program are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This program is licensed under the [MIT License](LICENSE).
