import sys

N = int(sys.stdin.readline())
cnt = [0]*10000
for _ in range(N):
    cnt[int(sys.stdin.readline())-1] += 1


for i in range(10000):
    for j in range(cnt[i]):
        sys.stdout.write(str(i+1))
        sys.stdout.write('\n')