import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

q = deque()

for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 1:
            q.append((y, x, 0))

res = 0
while q:
    cy, cx, d = q.popleft()
    res = max(res, d)

    for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ny, nx = cy + dy, cx + dx
        if 0 <= ny < N and 0 <= nx < M and tomatos[ny][nx] == 0:
            tomatos[ny][nx] = 1
            q.append((ny, nx, d+1))

for y in range(N):
    for x in range(M):
        if tomatos[y][x] == 0:
            res = -1
            
print(res)