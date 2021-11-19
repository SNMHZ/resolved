# 이걸 DP로 어떻게 풀지..??

import sys
from collections import deque

N = int(sys.stdin.readline())

q = deque()
q.append((N, str(N)))

while q:
    n, path = q.popleft()
    if n == 1:
        print(len(path.split())-1)
        print(path)
        break
    else:
        q.append((n-1, path + ' ' + str(n-1)))
        if n % 2 == 0:
            q.append((n//2, path + ' ' + str(n//2)))
        if n % 3 == 0:
            q.append((n//3, path + ' ' + str(n//3)))