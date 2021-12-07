import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split())) + [0]

min_len = float('inf')
low, high = 0, 0
_sum = arr[0]

while high < N:
    if _sum < S:
        high += 1
        _sum += arr[high]
    else:
        min_len = min(min_len, (high - low)+1)
        _sum -= arr[low]
        low += 1
        if low > high:
            high = low

print(min_len if min_len != float('inf') else 0)