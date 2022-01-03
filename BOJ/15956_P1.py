import sys

S = sys.stdin.readline().strip().split('&&')

for s in S:
    isEqual = True
    if '==' in s:
        A, B = s.split('==')
    elif '!=' in s:
        A, B = s.split('!=')
        isEqual = False
    
    print(A, B, isEqual)