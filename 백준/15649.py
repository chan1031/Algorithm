n, m = map(int, input().split())
visited = [False] * (n+1)  # 방문 수열을 저장
sequence = []  # 만든 수열을 저장

def backtrack(start):
    # 수열이 m개가 되면 출력하고 종료
    if len(sequence) == m:
        print(' '.join(map(str, sequence)))
        return

    # 1부터 n까지 숫자를 시도
    for i in range(start, n+1):
        if not visited[i]:  # 아직 사용하지 않은 숫자라면
            visited[i] = True  # 방문 체크
            sequence.append(i)  # 수열에 추가
            backtrack(i)  # 다음 숫자 선택하러 가기
            sequence.pop()  # 수열에서 제거
            visited[i] = False  # 방문 체크 해제

backtrack(1)  # 재귀 함수 호출