#brute-force도 우아하게 짤 수 있을까..?

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M==0:
    disables=[]
else:
    disables = sys.stdin.readline().split()

if N-100==0:
    print(0)
elif M==10:
    print(abs(N-100))
else:
    disable_dict = {}
    for i in range(10):
        if str(i) not in disable_dict:
            disable_dict[str(i)] = False
    for dis in disables:
        disable_dict[dis] = True
    every_num_disabled = True
    for i in range(1, 10):
        every_num_disabled = every_num_disabled and disable_dict[str(i)]
    
    if every_num_disabled:
        print( min( abs(N-100), abs(N-0)+1 ) )
    else:
        def isMakeable(num: int):
            for c in str(num):
                if disable_dict[c]:
                    return False
            return True

        upN = N
        while not isMakeable(upN):
            upN+=1

        downN = N
        while not isMakeable(downN):
            downN-=1
            if downN < 0:
                downN = float('inf')
                break

        print( min( abs(N-100), abs(N-upN)+len(str(upN)), abs(N-downN)+len(str(downN))) )