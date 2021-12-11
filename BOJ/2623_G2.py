import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
vertex = [ [] for _ in range(0, N+1) ]
fan_in = [ 0 for _ in range(0, N+1) ]

for _ in range(M):
    data = list(map(int, sys.stdin.readline().split()))[1:]
    for i in range(len(data)-1):
        if data[i+1] not in vertex[data[i]]:
            vertex[data[i]].append(data[i+1])
            fan_in[data[i+1]] += 1

q = deque()
for i in range(1, N+1):
    if fan_in[i] == 0:
        q.append(i)

res = []
while q:
    e = q.popleft()
    res.append(e)
    for i in vertex[e]:
        fan_in[i] -= 1
        if fan_in[i] == 0:
            q.append(i)

if len(res) == N:
    print(*res)
else:
    print(0)