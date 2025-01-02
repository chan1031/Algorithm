import sys

# 입력받을 테스트 케이스 개수
T = int(sys.stdin.readline().strip())

# 각 테스트 케이스에 대해 처리
for _ in range(T):
    # 괄호 문자열 입력받기
    ps = sys.stdin.readline().strip()

    # 스택을 이용하여 VPS 검사
    stack = []
    is_vps = True  # 올바른 VPS인지 여부

    for char in ps:
        if char == '(':
            stack.append(char)
        elif char == ')':
            # 닫힌 괄호가 있을 때, 스택이 비어있으면 올바르지 않음
            if not stack:
                is_vps = False
                break
            stack.pop()

    # 스택이 비어 있지 않으면 올바르지 않은 괄호 문자열
    if stack:
        is_vps = False

    # 결과 출력
    if is_vps:
        print("YES")
    else:
        print("NO")
