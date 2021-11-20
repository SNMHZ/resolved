import sys
from collections import deque

N = int(sys.stdin.readline())

## BFS
q = deque()
q.append((N, str(N)))

while q:
    n, path = q.popleft()
    if n == 1:
        print(len(path.split())-1)
        print(path)
        break
    else:
        q.append((n-1, path + ' ' + str(n-1)))
        if n % 2 == 0:
            q.append((n//2, path + ' ' + str(n//2)))
        if n % 3 == 0:
            q.append((n//3, path + ' ' + str(n//3)))

# ## DP(Bottom-Up)
# dp = [0] * (N+1)
# path_arr = [0] * (N+1)

# for i in range(1, N+1):
#     dp[i] = dp[i-1] + 1
#     path_arr[i] = i-1
#     if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
#         dp[i] = dp[i//2]+1
#         path_arr[i] = i//2
#     if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
#         dp[i] = dp[i//3]+1
#         path_arr[i] = i//3

# path = []
# while N != 0:
#     print(N, end=' ')
#     path.append(N)
#     N = path_arr[N]

# # print(' '.join(map(str, path)))