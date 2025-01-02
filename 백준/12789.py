n = int(input())
sequence = list(map(int, input().split()))

stack = []
expected = 1  # 기대하는 숫자
result = []

for num in sequence:
    stack.append(num)  # 숫자를 스택에 추가

    # 스택의 최상단 숫자가 기대하는 숫자와 일치하는지 확인
    while stack and stack[-1] == expected:
        result.append(stack.pop())  # 일치하면 스택에서 꺼내기
        expected += 1  # 다음 기대 숫자로 증가

# 결과 출력
if result == list(range(1, n + 1)):
    print("Nice")
else:
    print("Sad")
