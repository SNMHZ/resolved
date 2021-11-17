import sys

N = int(sys.stdin.readline())
mod = 1000000000

dp = [ [ [0,0,0,0] for _ in range(10) ] for _ in range(N) ]

for i in range(1, 9):
    dp[0][i][0] = 1
dp[0][9][0b10] = 1

for i in range(1, N):
    for j in range(4):
        dp[i][0][(j|0b01)] += dp[i-1][1][j]%mod
        dp[i][9][(j|0b10)] += dp[i-1][8][j]%mod
        for k in range(1, 9):
            dp[i][k][j] += dp[i-1][k-1][j]%mod
            dp[i][k][j] += dp[i-1][k+1][j]%mod

print(sum([ i[0b11] for i in dp[N-1]])%mod)