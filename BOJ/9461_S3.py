import sys


arr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
cur = len(arr)

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    if N < cur:
        print(arr[N-1])
    else:
        while cur < N:
            arr.append(arr[cur-2] + arr[cur-3])
            cur += 1
        print(arr[N-1])