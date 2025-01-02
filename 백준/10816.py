import sys
#상근이가 가진 카드의 개수
n = int(sys.stdin.readline().rstrip())
#상근이가 가진 카드의 값
n_cards = list(sys.stdin.readline().rstrip().split())
#맞출 카드의 개수
m = int(sys.stdin.readline().rstrip())
#맞출 카드의 값
m_cards = list(sys.stdin.readline().rstrip().split())

#상근이가 가진 카드를 딕셔너리에 저장
dic = {}
for i in n_cards:
  if i in dic:
    dic[i] += 1
  else:
    dic[i] = 1

#카드 맞추기
for j in m_cards:
  if j in dic:
    print(dic[j], end=' ')
  else:
    print('0', end=' ')
