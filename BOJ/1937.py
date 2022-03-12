## interpreter: python3

import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]

def dfs(y, x) -> int:
    if dp[y][x] != 0:
        return dp[y][x]
    
    dp[y][x] = 1
    cur_max = 0
    for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ny, nx = y + dy, x + dx
        if 0 <= ny < n and 0 <= nx < n and board[ny][nx] > board[y][x]:
            dfs_res = dfs(ny, nx)
            if dfs_res > cur_max:
                cur_max = dfs_res
            # cur_max = max(cur_max, dfs(ny, nx))
    dp[y][x] += cur_max

    return dp[y][x]

max_depth = 0
for y in range(n):
    for x in range(n):
        max_depth = max(max_depth, dfs(y, x))

# print(*dp, sep='\n')
print(max_depth)