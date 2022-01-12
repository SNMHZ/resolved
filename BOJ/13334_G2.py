import sys
from heapq import heappush, heappop

N = int(sys.stdin.readline())
datas = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a >= b:
        heappush(datas, (a, b))
    else:
        heappush(datas, (b, a))
D = int(sys.stdin.readline())


lines_in = []
_max = 0
while datas:
    a, b = heappop(datas)
    if a-D <= b:
        heappush(lines_in, b)
    while lines_in and lines_in[0] < a-D:
        heappop(lines_in)
    _max = max(_max, len(lines_in))

print(_max)