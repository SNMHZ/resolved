import sys

N = int(sys.stdin.readline())
points = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]

def ccw(stand, p1, p2):
    return (p2[0]-stand[0])*(p1[1]-stand[1]) - (p1[0]-stand[0])*(p2[1]-stand[1])


res = 0
a = points[0]
for i in range(1, N-1):
    res += ccw(a, points[i], points[i+1])

print(abs(res/2))