import heapq

def astar(graph, start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0, start))

    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor in graph[current]:
            temp_g = g_score[current] + 1

            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score = temp_g + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_score, neighbor))

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.insert(0, current)
    return path
