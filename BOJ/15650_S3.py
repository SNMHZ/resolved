import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())

arr = [ i for i in range(1, N+1) ]
for comb in combinations(arr, M):
    print(*comb)