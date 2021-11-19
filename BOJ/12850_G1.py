import sys

m_dict = {0:'정보섬', 1:'전산관', 2:'미래관', 3:'신양관', 4:'한경직기념관', 5:'진리관', 6:'형남공학관', 7:'학생회관'}
mm_dict = dict([(value, key) for key, value in m_dict.items()])

gr = {'정보섬':['전산관', '미래관'], 
'전산관':['정보섬', '미래관', '신양관'], 
'미래관':['정보섬', '전산관', '신양관', '한경직기념관'], 
'신양관':['전산관', '미래관', '한경직기념관', '진리관'], 
'한경직기념관':['미래관', '신양관', '진리관', '형남공학관'], 
'진리관':['신양관', '한경직기념관', '학생회관'], 
'형남공학관':['학생회관', '한경직기념관'], 
'학생회관':['형남공학관', '진리관']}

D = int(sys.stdin.readline())

mat = [[0]*8 for _ in range(8)]

for i in range(8):
    for j in gr[m_dict[i]]:
        mat[i][mm_dict[j]] = 1

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

print(matrix_power(mat, D)[0][0])