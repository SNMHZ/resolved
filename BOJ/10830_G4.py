import sys

N, B = map(int, sys.stdin.readline().split())
A = [ list(map(int, sys.stdin.readline().split())) for _ in range(N) ]


def matrix_mul(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000
    return C

def matrix_power(mat, n, start):
    if n == 1:
        return mat

    a = matrix_power(mat, n//2, start)
    res = matrix_mul(a, a)

    if n % 2 == 1:
        res = matrix_mul(res, start)
    return res

ans = matrix_power(A, B, A)

for i in range(len(ans)):
    print(*list(map(lambda x: x%1000, ans[i])))