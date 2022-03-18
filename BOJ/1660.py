import sys

N = int(sys.stdin.readline())

tri, cnt = 0, 0
arr = []
for i in range(1, N+1):
    tri += i
    cnt += tri
    
    if cnt > N:
        break
    arr.append(cnt)

dp = [N] * (N+1)
dp[0] = 0

for a in arr[::-1]:
    dp[a] = 1
    for i in range(a, N+1):
        if i+a <= N:
            dp[i+a] = min(dp[i] + 1, dp[i+a])

print(dp[N])

# q = deque([(a, 1) for a in arr])

# while q:
#     cur, depth = q.popleft()
#     if cur == N:
#         print(depth)
#         break
#     for a in arr:
#         if cur+a <= N:
#             q.append((cur+a, depth+1))