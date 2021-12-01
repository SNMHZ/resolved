import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
vertex = [ [] for _ in range(0, N+1) ]
fan_in = [ 0 for _ in range(0, N+1) ]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    vertex[a].append(b)
    fan_in[b] += 1

q = deque()
for i in range(1, N+1):
    if fan_in[i] == 0:
        q.append(i)

while q:
    e = q.popleft()
    print(e, end=' ')
    for i in vertex[e]:
        fan_in[i] -= 1
        if fan_in[i] == 0:
            q.append(i)