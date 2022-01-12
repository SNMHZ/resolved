import sys

N = int(sys.stdin.readline())
datas = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    if a <= b:
        datas.append([a, b])
    else:
        datas.append([b, a])
#datas = sorted(datas, key=lambda x: x[1])
datas = sorted(datas, key=lambda x: x[0])

cur = [ datas[0][:] ]
for i in range(1, N):
    if datas[i][0] <= cur[-1][1]:
        cur[-1][1] = max(cur[-1][1], datas[i][1])
    else:
        cur.append(datas[i][:])

_len = 0
for i in range(len(cur)):
    _len += cur[i][1] - cur[i][0]

print(_len)