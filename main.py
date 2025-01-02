import sys

#재귀 깊이를 제한: 배추밭의 크기가 50x50 = 2500이면 최악의 경우 2500번 이상 재귀를 호출해야 할 수 있는데
#파이썬의 경우 기본적으로 재귀함수는 1000번까지만 제한하기 때문에 늘려줄 필요가 있다.
sys.setrecursionlimit(10000)

T = int(input()) #테스트 케이스 입력

def dfs(x,y):
    #지정된 구역을 벗어났을 경우
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    #해당 구역에 배추가 있는 경우
    if field[y][x] == 1:
        field[y][x] = 0 #방문처리
        
        #재귀함수로 상하좌우 탐색
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    #배추가 없는 경우    
    return False        

#입력 받기
for _ in range(T):
    m, n , k = map(int, input().split()) #배추 밭의 크기와 배추 개수 입력

    field = [[0] * m for _ in range(n)] # 가로 M, 세로 N 만큼의 0으로 초기화 된 배추밭 만들기

    for _ in range(k):
        X,Y = map(int, input().split())
        field[Y][X] = 1 #배추가 있는 곳을 1로 초기화

    result = 0
    for i in range(n):
        for j in range(m):
            if dfs(j,i):
                result +=1

    print(result)
    


        


