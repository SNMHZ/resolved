import sys

N = int(sys.stdin.readline())
edges = [ list(map(int, sys.stdin.readline().split())) for _ in range(N-1) ]
M = int(sys.stdin.readline())
quarry = [ list(map(int, sys.stdin.readline().split())) for _ in range(M) ]

print(edges)
print(quarry)