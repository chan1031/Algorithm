import sys
from math import gcd

n = int(sys.stdin.readline().strip())

number = int(sys.stdin.readline().strip())
array=[]
#가로수간의 간격을 저장한다.
for i in range(n-1):
  flag = int(sys.stdin.readline().strip())
  array.append(flag - number)
  number = flag  

g= array[0]
#간격 배열에 저장된 값들의 최대 공약수를 구한다.
for i in range(1,len(array)):
  g = gcd(array[i], g)  

#구한 최대공약수 간격으로 가로수를 배치한다.
count =0
for each in array:
  count += each//g-1
print(count)


