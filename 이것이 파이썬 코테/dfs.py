def dfs(graph, v, visited):
  visited[v] = True
  print(v, end='')

  for i in graph[v]:
    if not visited[i]:
      dfs(graph, i, visited)


graph = [[], [2, 3, 8], [1, 7], [1, 4, 5]]

visited = [False] * 9
