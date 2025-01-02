import sys

n, m = map(int, sys.stdin.readline().split())
n_cards = list(sys.stdin.readline().rstrip().split())
m_cards = list(sys.stdin.readline().rstrip().split())

n_dic={}
m_dic={}
count=0
#A-B
for i in n_cards:
  if i in n_dic:
    n_dic[i] +=1
  else:
    n_dic[i]=1

for j in m_cards:
  if j in n_dic:
    count+=n_dic[j]

n=n-count
count=0

#B-A
for j in m_cards:
  if j in m_dic:
    m_dic[j]+=1
  else:
    m_dic[j]=1
for i in n_cards:
  if i in m_dic:
    count+=m_dic[i]

m=m-count

print(n+m)

#딕셔너리의 새로운 접근법
'''
for key,value in dic.items():
위 반복문은 딕셔너리의 순서대로 key와 value값을 가지고 오는 반복문이다.
'''
