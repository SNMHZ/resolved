# https://www.acmicpc.net/problem/2447
# https://chatgpt.com/share/bfb3af54-4003-4f02-8283-9279fad8abf7
# 어지러운 세상이다...

import sys

N = int(sys.stdin.readline())

def draw_star(n):
    if n == 1:
        return ['*']
    
    stars = draw_star(n // 3)
    L = []
    
    for s in stars:
        L.append(s * 3)
    for s in stars:
        L.append(s + ' ' * (n // 3) + s)
    for s in stars:
        L.append(s * 3)
    
    return L

def print_star(n):
    pattern = draw_star(n)
    for line in pattern:
        print(line)


print_star(N)
