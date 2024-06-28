#이번엔 이진탐색을 사용해서 풀어본다 이진탐색의 경우 O(logn)의 매우 빠른속도로 해당되는 값의 인덱스를 반환한다.

import bisect

# 상근이가 가지고 있는 카드의 개수
N = int(input())

# 상근이가 가지고 있는 카드들
cards = list(map(int, input().split()))
cards.sort()  # 이분 탐색을 위해 정렬

# 다른 카드들의 개수
M = int(input())

# 다른 카드들의 숫자들
others = list(map(int, input().split()))

# 결과 리스트
result = []

# 다른 카드 숫자들에 대해 이분 탐색 수행
for num in others:
    # bisect_left를 사용하여 num이 cards에 존재하는지 확인
    index = bisect.bisect_left(cards, num)
    if index < N and cards[index] == num:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(" ".join(map(str, result)))
