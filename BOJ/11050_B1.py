import sys

N, K = map(int, sys.stdin.readline().split())
MOD = 10007

res = 1

for i in range(N, N-K, -1):
    res *= i
    res %= MOD

for i in range(2, K+1):
    res //= i

print(res)