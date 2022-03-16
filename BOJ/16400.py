import sys

N = int(sys.stdin.readline())
mod = 123456789

arr = [True] * (N+1)
coins = []

for i in range(2, N + 1):
    if arr[i] == True:
        coins.append(i)
        j = 2

        while (i * j) <= N:
            arr[i*j] = False
            j += 1

# for num in range(2, N+1):
#     for i in range(2, int(num**0.5)+1):
#         if num % i == 0:
#             break
#     else:
#         coins.append(num)

# print(coins)

dp = [0] * (N+1)
dp[0] = 1

for coin in coins:
    for i in range(coin, N+1):
        dp[i] += dp[i-coin]
        dp[i] %= mod

print(dp[N])

# arr[0] = arr[1] = 0
# dp = [0] * (N+1)

# for i in range(N+1):
#     if arr[i]:
#         for j in range(i, N+1):
#             if arr[j] and i+j<=N:
#                 dp[i+j] += arr[i] 

# print([i for i in range(N+1)])
# print(arr)
# print(dp)

# # arr = dp
# cur_dp = [0] * (N+1)

# for i in range(N+1):
#     if arr[i]:
#         for j in range(i, N+1):
#             if dp[j] and i+j<=N:
#                 print(i, j)
#                 cur_dp[i+j] += dp[i]+arr
# print('==')
# print([i for i in range(N+1)])
# print(arr)
# print(dp)
# print(cur_dp)