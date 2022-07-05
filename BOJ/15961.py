import sys

N, d, k, c = map(int, sys.stdin.readline().split())
sushi_data = [ int(sys.stdin.readline()) for _ in range(N) ]

sushi = [0] * (d+1)
cur_cnt = 0
answer = 0
for i in range(k):
    if sushi[sushi_data[i]] == 0:
        cur_cnt += 1
    sushi[sushi_data[i]] += 1
answer = max(answer, cur_cnt if sushi[c] > 0 else cur_cnt+1)

for i in range(N):
    start, end = i, i+k if i+k < N else i+k-N
    if sushi[sushi_data[start]] == 1:
        cur_cnt -= 1
    sushi[sushi_data[start]] -= 1

    if sushi[sushi_data[end]] == 0:
        cur_cnt += 1
    sushi[sushi_data[end]] += 1

    answer = max(answer, cur_cnt if sushi[c] > 0 else cur_cnt+1)

print(answer)