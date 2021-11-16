import sys

N = int(sys.stdin.readline())
A = [[1,1],[1,0]]

def matrix_mul(A, B):
    C = [[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] %= 1000000007
    return C

def matrix_power(mat, n):
    if n == 1:
        return mat

    a = matrix_power(mat, n//2)
    res = matrix_mul(a, a)

    if n % 2 == 1:
        res = matrix_mul(res, mat)
    return res

if N == 1:
    print(1)
else:
    print(matrix_power(A, N-1)[0][0])