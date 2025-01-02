import math

def sieve_of_eratosthenes(m, n):
    # n까지의 소수를 찾기 위한 리스트 생성
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False  # 0과 1은 소수가 아님

    # 에라토스테네스의 체 알고리즘
    for p in range(2, int(math.sqrt(n)) + 1):
        if is_prime[p]:
            # p의 배수들을 False로 설정
            for i in range(p * p, n + 1, p):
                is_prime[i] = False

    # m부터 n까지의 소수를 리스트에 저장
    prime_numbers = []
    for p in range(max(2, m), n + 1):
        if is_prime[p]:
            prime_numbers.append(p)

    return prime_numbers

# n, m을 입력받는다.
m, n = map(int, input().split())
array_check = sieve_of_eratosthenes(m, n)

# 소수를 출력
for i in array_check:
    print(i)
