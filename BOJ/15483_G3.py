import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
for i in range(1, len(str2) + 1):
    dp[0][i] = i
for i in range(1, len(str1) + 1):
    dp[i][0] = i

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

print(dp[-1][-1])