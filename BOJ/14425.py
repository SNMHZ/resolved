import sys

N, M = map(int, sys.stdin.readline().split())

_set = set([sys.stdin.readline().strip() for _ in range(N)])

cnt = 0
for _ in range(M):
    if sys.stdin.readline().strip() in _set:
        cnt += 1

print(cnt)