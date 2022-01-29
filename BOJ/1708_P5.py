import sys
from functools import cmp_to_key

N = int(sys.stdin.readline())
points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(N)]

# convex_hull. graham scan
def convex_hull(points):
    _points = sorted(points, key=lambda x: (x[1], x[0]))
    stack = [_points[0]]
    def _ccw(a, b, c): return a[0]*b[1] + b[0]*c[1] + c[0]*a[1] - b[0]*a[1] - c[0]*b[1] - a[0]*c[1]
    def _dist(a, b): return (a[0]-b[0])**2 + (a[1]-b[1])**2
    def _cmp(a, b):
        c = _ccw(_points[0], a, b)
        if c != 0: return -c
        return _dist(a, _points[0]) - _dist(b, _points[0])
    _points = sorted(_points[1:], key=cmp_to_key(_cmp))
    for i in range(len(_points)):
        while len(stack) >= 2 and _ccw(_points[i], stack[-2], stack[-1]) <= 0: stack.pop()
        stack.append(_points[i])
    
    return stack

print(len(convex_hull(points)))