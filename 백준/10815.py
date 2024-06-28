#상근이가 가지고 있는 카드
n = map(int, input().split())
#상근이가 가지고 있는 카드들
cards = list(map(int,input().split()))

#다른 카드들의 개수
m = map(int, input().split())
#다른 카드들의 숫자들
others = list(map(int,input().split()))

#딕셔너리 설정
dic = {o:0 for o in others}
#ex) others가 [1,2,3]이면 dic = {1:0, 2:0, 3:0}으로 초기화 됨
#여기서 0 부분은 상근이와 겹치고 있는지의 여부임

#상근이의 카드와 비교
# cards의 값인 c를 뽑음
for c in cards:
  if c in dic:
      dic[c] = 1 # 딕셔너리의 cards의 c에 해당되는 키의 값을 1로 설정한다.

for d in dic:
  print(dic[d], end=' ')









