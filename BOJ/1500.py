import sys

S, K = map(int, sys.stdin.readline().split())

res = 1
while K:
    res *= S // K
    S -= (S // K)
    K -= 1

print(res)