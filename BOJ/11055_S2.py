import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sub_sum = [ i for i in arr]

sub_arr = [[]] * N
sub_arr[0] = [arr[0]]

for i in range(1, N):
    for j in range(i):
        if arr[i] > arr[j] and sub_sum[i] < sub_sum[j] + arr[i]:
            sub_arr[i] = sub_arr[j] + [arr[i]]
            sub_sum[i] = sub_sum[j] + arr[i]

print(max(sub_sum))