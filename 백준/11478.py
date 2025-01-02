import sys

S = input()

cnt = set()

data_length = len(S)

for i in range(data_length):
    for j in range(i+1, data_length+1):
      print(S[i:j])  
      cnt.add(S[i:j])

print(cnt)
print(len(cnt))