from bfs import bfs
from dfs import dfs
from astar import astar

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def heuristic(n, goal):
    return 1

def main():
    print("1. BFS\n2. DFS\n3. A*")
    choice = int(input("Enter choice: "))

    if choice == 1:
        print(bfs(graph, 'A', 'F'))
    elif choice == 2:
        print(dfs(graph, 'A', 'F'))
    elif choice == 3:
        print(astar(graph, 'A', 'F', heuristic))

if __name__ == "__main__":
    main()
