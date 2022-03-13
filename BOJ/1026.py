import sys

N = int(sys.stdin.readline())
arr1 = sorted(map(int, sys.stdin.readline().split()))
arr2 = sorted(map(int, sys.stdin.readline().split()), reverse=True)

print(sum([a1*a2 for a1, a2 in zip(arr1, arr2)]))