import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
points = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

# graham scan
def ccw(a, b, c):
    return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1]

def convex_hull(points):
    _points = sorted(points, key=lambda x: (x[1], x[0]))
    stack = [_points[0]]
    def _cmp(a, b):
        c = ccw(_points[0], a, b)
        if c != 0:
            return c < 0
        return (a[0] - _points[0][0])**2 + (a[1] - _points[0][1])**2 > (b[0] - _points[0][0])**2 + (b[1] - _points[0][1])**2

    _points = sorted(_points[1:], key=cmp_to_key(_cmp))
    print(_points)
    for i in range(len(_points)):
        while len(stack) >= 2 and ccw(_points[i], stack[-2], stack[-1]) <= 0:
            print(stack)
            stack.pop()
        stack.append(_points[i])
    return stack

print(convex_hull(points))
print(len(convex_hull(points)))