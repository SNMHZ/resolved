import sys

N = int(sys.stdin.readline())

count = 0
count += N//5
N %= 5

count += N//3
N %= 3

if N == 0:
    print(count)
else:
    print(-1)