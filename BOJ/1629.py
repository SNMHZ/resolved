import sys

A, B, C = map(int, sys.stdin.readline().split())

def exp(x, n):
    x %= C
    if n == 0:
        return 1
    if n == 1:
        return x%C
    if n % 2 == 0:
        return exp(x*x, n//2)%C
    else:
        return x * exp(x*x, (n-1)//2)%C


print(exp(A, B))