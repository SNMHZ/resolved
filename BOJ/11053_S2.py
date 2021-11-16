import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j]: # 11722는 부호 반대로
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))