import sys

N = int(sys.stdin.readline())

for i in range(N):
    print(' '*(N-1-i)+'*'*(i+1) ) 