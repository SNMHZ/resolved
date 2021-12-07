import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

low, high = 0, 0
count = 0
arr.append(0)
_sum = arr[0]
while high < N:
    if _sum < M:
        high += 1
        _sum += arr[high]
    elif _sum > M:
        _sum -= arr[low]
        low += 1
        if low > high:
            high = low
            _sum = arr[low]
    else:
        count += 1
        high += 1
        _sum += arr[high]

print(count)