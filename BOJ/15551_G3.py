import sys

N = int(sys.stdin.readline())

a = 'a'*N

h = 0
for i in range(N):
    h = 31*h + ord(a[i])

b = ''
for i in range(N-1):
    b += chr(h%26+ord('b'))
    h = h//26-ord('b')

b += chr(h)
print(chr(h))

print(b, h)