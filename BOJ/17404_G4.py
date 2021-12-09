import sys

N = int(sys.stdin.readline())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
R, G, B = 0, 1, 2

ans = float('inf')
for color in [R, G, B]:
    dp = [[float('inf')] * 3 for _ in range(N)]

    dp[0][color] = data[0][color]
    for i in range(1, N):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + data[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + data[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + data[i][B]
    dp[N-1][color] = float('inf')
    ans = min(dp[-1]+[ans])
print(ans)