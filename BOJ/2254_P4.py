import sys
from functools import cmp_to_key

N, px, py = map(int, sys.stdin.readline().split())
dots = set([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])

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

def isInside(dots, x, y) -> bool:
    if len(dots) < 3: return False
    def ccw(a, b, c):
        cw = (a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
        if cw > 0: return 1
        elif cw < 0: return -1
        else: return 0
    cwb = ccw(dots[0], dots[1], (x, y))
    for i in range(1, len(dots)):
        cw = ccw(dots[i-1], dots[i], (x, y))
        if cw != cwb:
            return False
    return True
    
cnt = 0
while True:
    if len(dots) >= 3:
        cur_convex = convex_hull(dots)
    else:
        break
    if isInside(cur_convex, px, py):
        cnt += 1
        dots-=set(cur_convex)
    else:
        break

print(cnt)