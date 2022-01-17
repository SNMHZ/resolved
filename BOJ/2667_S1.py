import sys
from collections import deque

N = int(sys.stdin.readline())

board = [ list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N) ]
visited = [[0] * N for _ in range(N)]

q = deque()
num = 0
cnt_list = []

for y in range(N):
    for x in range(N):
        if board[y][x] == 1 and visited[y][x] == 0:
            num += 1
            cnt = 1
            visited[y][x] = num
            q.append((y, x))
            
            while q:
                cur_y, cur_x = q.popleft()
                for dy, dx in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                    ny, nx = cur_y + dy, cur_x + dx
                    if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] == 0 and board[ny][nx] == 1:
                        cnt += 1
                        visited[ny][nx] = num
                        q.append((ny, nx))
                        
            cnt_list.append(cnt)



print(num)
print(*sorted(cnt_list), sep='\n')