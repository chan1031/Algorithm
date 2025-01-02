import sys
from collections import deque

N = int(input())

d = deque()

for i in range(N):
    flag = int(sys.stdin.readline())

    #0일 경우
    if flag == 0:
        if len(d) !=0:
            #deque.pop()시에는 항상 deque가 비어있지 않은지 체크해야한다.
            d.pop()
    else:
        d.append(flag)

sum=0
for j in range(len(d)):
    sum += d[j]
print(sum)
