import sys
from heapq import heappush, heappop, heapify

n = int(sys.stdin.readline())

minheap = list(map(int, sys.stdin.readline().split()))
heapify(minheap)

for _ in range(n-1):
    for i in map(int, sys.stdin.readline().split()):
        if minheap[0] < i:
            heappush(minheap, i)
            heappop(minheap)


print(minheap[0])