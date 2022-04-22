import sys

L, U = map(int, sys.stdin.readline().split())

res = [0]*10
start = L
end = U
digit = 1

def cal(n, d):
    while n > 0:
        res[n%10] += d
        n //= 10

while start <= end:

    while end%10 != 9 and start <= end:
        cal(end, digit)
        end -= 1
    
    if start > end:
        break

    while start%10 != 0 and start <= end:
        cal(start, digit)
        start += 1
    
    start //= 10
    end //= 10

    for i in range(10):
        res[i] += (end-start+1)*digit
    
    digit *= 10

print(sum([ res[i]*i for i in range(10) ]))