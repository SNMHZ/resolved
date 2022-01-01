import sys

N, M = map(int, sys.stdin.readline().split())
data = dict([sys.stdin.readline().split() for _ in range(N)])
tc = [ sys.stdin.readline().strip() for _ in range(M) ]

for t in tc:
    print(data[t])
