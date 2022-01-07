import sys
A, B, V = map(int, sys.stdin.readline().split())
print( (V-A)//(A-B) + 2 if (V-A)%(A-B) else (V-A)//(A-B) + 1 )