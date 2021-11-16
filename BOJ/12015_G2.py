# 12738 동일

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

lis = [ arr[0] ]
count = 1

for i in range(1, N):
    if arr[i] > lis[-1]:
        lis.append(arr[i])
        count += 1
    else:
        left = 0
        right = len(lis) - 1
        while left <= right:
            mid = (left + right) // 2
            if lis[mid] < arr[i]:
                left = mid + 1
            else:
                right = mid - 1
        lis[left] = arr[i]

print(count)