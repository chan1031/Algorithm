n, m = map(int, input().split())

graph = []
for i in range(n):
  graph.append(list(map(int, input())))


# dfs 함수 정의
def dfs(x, y):
  # 주어진 범위를 벗어나면 즉시 종료
  if x < 0 or x >= n or y < 0 or y >= m:
    return False

  # 현재 노드가 0인가?
  if graph[x][y] == 0:
    # 현재 노드 값이 0이면 1로 표기하여 방문처리
    graph[x][y] = 1
    # 상하좌우의 dfs 실시
    dfs(x + 1, y)
    dfs(x - 1, y)
    dfs(x, y + 1)
    dfs(x, y - 1)
    return True

  # 현재 노드 값이 1이면 그냥 나가기
  return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i, j):
      result += 1

print(result)

