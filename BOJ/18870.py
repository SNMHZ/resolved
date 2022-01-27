import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
chg = dict([ (k, i) for (i, k) in enumerate(sorted(list(set(arr)))) ])

print(*[ chg[k] for k in arr ])