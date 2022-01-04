import sys

# def hh(a):
#         h = 0
#         for i in range(N):
#             h = 31*h + ord(a[i])
#         return h

# for N in range(2, 101):
#     A = 's'*(N-2)+'Ao'
#     B = 's'*(N-2)+'BP'

#     assert hh(A) == hh(B)

N = int(sys.stdin.readline())

print('s'*(N-2)+'Ao')
print('s'*(N-2)+'BP')