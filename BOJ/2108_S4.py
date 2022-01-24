import sys


N = int(sys.stdin.readline())
data = [ int(sys.stdin.readline()) for _ in range(N) ]

data.sort()

print(int(round(sum(data)/N, 0)))
print(data[int(N/2)])

cnt = {}
for i in data:
    if i not in cnt:
        cnt[i] = 1
    else:
        cnt[i] += 1

cnt = sorted(list(cnt.items()) , key=lambda x: x[1], reverse=True)
if N > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])

print(abs(min(data)-max(data)))