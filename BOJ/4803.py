import sys

cnt = 1
while True:
    N, M = map(int, sys.stdin.readline().split())
    if N == 0 and M == 0:
        break
    edges = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]
    cnt += 1
    print(edges)
    print(cnt)
    

