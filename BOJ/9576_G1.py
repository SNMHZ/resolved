# Greedy. 이분매칭 쓰지 않았음

import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr = sorted([tuple(map(int, sys.stdin.readline().split())) for _ in range(M)], key=lambda x: x[0])
    arr.sort(key=lambda x: x[1])

    cur = 1
    count = 0
    books = [False] * (N+1)
    for a, b in arr:
        for i in range(a, b+1):
            if not books[i]:
                books[i] = True
                count += 1
                break
    print(count)