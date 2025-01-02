from collections import deque

#N,M 을 입력 
N, M = map(int, input().split())
# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(N):
  graph.append(list(map(int, input())))

#이동할 방향을 정의한다.
dx =[-1,1,0,0]
dy = [-1,1,0,0]

#BFS 구현
def bfs(x,y):
  #큐 구현을 위한 deque
  queue = deque()
  queue.append((x,y))
  #큐가 빌 때까지 반복
  while queue:
    x,y = queue.popleft()
    #현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx <0 or  y<0 or nx>=N or ny>=M:
          continue
      #벽인 경우도 무시
      if graph[nx][ny] == 0:
          continue
    #해당 노드를 처음 방분하는 경우메나 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] +1
        queue.append((nx,ny))
    #가장 오른쪽 아래까지의 최단거리를 반환
    return graph[N-1][M-1]

#BFS 출력 결과
print(bfs(0,0))




