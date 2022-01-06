import sys
from collections import deque

N = int(sys.stdin.readline())
sx, sy, ex, ey = map(int, sys.stdin.readline().split())

visited = [[False]*N for _ in range(N)]

q = deque()
q.append((sx, sy, 0))
visited[sx][sy] = True

res = -1
while q:
    x, y, depth = q.popleft()
    if x == ex and y == ey:
        res = depth
        break
    for dx, dy in ((-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)):
        nx, ny = x+dx, y+dy
        if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
            q.append((nx, ny, depth+1))
            visited[nx][ny] = True

print(res)