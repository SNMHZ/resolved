import sys

N = int(sys.stdin.readline())
datas = sorted(list(map(int, sys.stdin.readline().split())))

MOD = 1000000007
res = 0
mul = 1
for i in range(1,N):
    res += (datas[i]-datas[-i-1])*mul%MOD
    res %= MOD
    mul = ((mul+1)*2-1 )%MOD

print(res)