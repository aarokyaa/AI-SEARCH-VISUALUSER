def dfs(graph, start, goal, path=[]):
    path = path + [start]

    if start == goal:
        return path

    for node in graph[start]:
        if node not in path:
            newpath = dfs(graph, node, goal, path)
            if newpath:
                return newpath
