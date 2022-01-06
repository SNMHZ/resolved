import sys
from functools import cmp_to_key

N, px, py = map(int, sys.stdin.readline().split())
dots = set([tuple(map(int, sys.stdin.readline().split())) for _ in range(N)])



def dotmul(a, b):
    return a[0]*b[1] - a[1]*b[0]

def dotsub(a, b):
    return (a[0]-b[0], a[1]-b[1])

def cmp(a, b):
    if dotmul(a, b):
        return dotmul(a, b) < 0
    return (a[0]**2 + a[1]**2) < (b[0]**2 - b[1]**2)

def convex_hull(dots):
    dots = sorted(dots)
    _dots = [(x-dots[0][0], y-dots[0][1]) for x, y in dots]
    stack = [_dots[0], _dots[1]]
    _dots = sorted(_dots[2:], key=cmp_to_key(cmp))
    
    for i in range(len(_dots)):
        while len(stack) >= 2 and dotmul(dotsub(stack[-1], stack[-2]), dotsub(stack[-1], _dots[i])) < 0:
            stack.pop()
        stack.append(_dots[i])
    return [(x+dots[0][0], y+dots[0][1]) for x, y in stack]

def ccw(a, b, c):
    cw = (a[0]*b[1]+b[0]*c[1]+c[0]*a[1]) - (a[1]*b[0]+b[1]*c[0]+c[1]*a[0])
    if cw > 0:
        return 1
    elif cw < 0:
        return -1
    else:
        return 0

def isInside(dots, x, y) -> bool:
    if len(dots) < 3:
        return False
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
    print(cur_convex)
    if isInside(cur_convex, px, py):
        cnt += 1
        dots-=set(cur_convex)
        print(dots)
    else:
        break

print(cnt)