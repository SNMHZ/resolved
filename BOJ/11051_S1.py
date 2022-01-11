import sys

N, K = map(int, sys.stdin.readline().split())

dp = [[0] * (N+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(0, N):
    for j in range(0, i+1):
        dp[i+1][j] += dp[i][j]
        dp[i+1][j] %= 10007
        dp[i+1][j+1] += dp[i][j]
        dp[i+1][j+1] %= 10007

print(dp[N][K])