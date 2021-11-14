import sys

input = sys.stdin.readline

n, B = 2, int(input())
A = [[1,1],[1,0]]

def power(a,b,n):
    cal = []
    for i in range(n):
        temp = []
        for j in range(n):
            num = 0
            for k in range(n):
                num += a[i][k] * b[k][j]
            temp.append(num%1000000007)
        cal.append(temp)
    return cal
count = 0
def dac(s,b):
    if b == 1:
        return s
    
    a = dac(s,b//2)
    global count 
    count+=1
    print(count, a)
    cal = power(a,a,n)
    
    result = []
    if b % 2:
        result = power(cal,A,n)
    else:
        result = cal
        
    return result

print(dac(A,B)[0][1])