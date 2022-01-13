import sys

M = int(sys.stdin.readline())
MOD = 1000000007

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a % MOD
    if n % 2 == 0:
        return power(a, n // 2) ** 2 % MOD
    else:
        return power(a, n // 2) ** 2 * a % MOD

factorial = [1, 1]

while M:
    M -= 1

    N, K = map(int, sys.stdin.readline().split())

    # 페르마의 소정리
    # ((n−r)!r!)^(p−2) mod p

    while len(factorial) <= N:
        factorial.append(factorial[-1] * (len(factorial)) % MOD)

    print( factorial[N]*power(factorial[N-K] * factorial[K] % MOD, MOD - 2) % MOD)