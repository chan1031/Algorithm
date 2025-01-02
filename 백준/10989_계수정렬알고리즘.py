#계수정렬 알고리즘
import sys

input = sys.stdin.readline  # 입력을 빠르게 받기 위해

n = int(input())
count = [0] * 10001  # 0부터 10000까지의 수를 세기 위한 리스트

for _ in range(n):
    num = int(input())
    count[num] += 1  # 해당 숫자의 등장 횟수 증가

# 정렬된 결과 출력
for i in range(1, 10001):
  #count[i] >0 은 count[i]의 값이 존재한다는 뜻이다.
    if count[i] > 0:
      #등장한 횟수만큼 i를 출력시킨다.
        for _ in range(count[i]):
            print(i)