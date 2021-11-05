# deque는 통과, queue는 타임아웃..

import sys
from collections import deque

N = int(sys.stdin.readline())
space = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]
shark_size = 2
shark_ate = 0
shark_lifetime = 0
 

eatables = set()
not_eatables = set()
shark_pos = None
for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            space[i][j] = 0
            shark_pos = (i, j)
        elif space[i][j] != 0 and space[i][j] < shark_size:
            eatables.add((i, j))
        elif space[i][j] != 0 and space[i][j] >= shark_size:
            not_eatables.add((i, j))

def bfs(start, end):
    visited = [ [False] * N for _ in range(N) ]
    q = deque()
    q.append( (start[0], start[1], 0) )
    visited[start[0]][start[1]] = True

    while q:
        x, y, depth = q.popleft()
        for dx, dy in (0,1), (0,-1), (1,0), (-1,0):
            nx, ny = x+dx, y+dy
            if nx==end[0] and ny==end[1]:
                    return depth+1
            if 0<=nx<N and 0<=ny<N and space[nx][ny]<=shark_size and not visited[nx][ny]:
                q.append((nx, ny, depth+1))
                visited[nx][ny] = True
    return -1

while eatables:
    eatable_dists = []
    for eatable in eatables:
        dist = bfs(shark_pos, eatable)
        if dist != -1:
            eatable_dists.append((eatable, dist))
    if not eatable_dists:
        break

    eatable_dists.sort(key=lambda x:x[0][1])
    eatable_dists.sort(key=lambda x:x[0][0])
    eatable_dists.sort(key=lambda x:x[1])

    shark_pos = eatable_dists[0][0]
    space[shark_pos[0]][shark_pos[1]] = 0
    eatables.remove(shark_pos)
    shark_lifetime += eatable_dists[0][1]
    shark_ate+=1

    if shark_ate == shark_size:
        shark_ate=0
        shark_size+=1
        caneat = []
        for not_eatable in not_eatables:
            if space[not_eatable[0]][not_eatable[1]] < shark_size:
                caneat.append(not_eatable)
        
        for can in caneat:
            not_eatables.remove(can)
            eatables.add(can)

print(shark_lifetime)