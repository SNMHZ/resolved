# https://softeer.ai/practice/info.do?idx=1&eid=626

import sys

N, M = map(int, sys.stdin.readline().split())
rooms = { sys.stdin.readline().strip() : [False]*9 for _ in range(N) }
data = [ tuple(sys.stdin.readline().split()) for _ in range(M) ]


for (name, s, e) in data:
    s, e = int(s)-9, int(e)-9
    for i in range(s, e):
        rooms[name][i] = True

names = sorted(rooms.keys())

for name in names:
    emps = []

    isBeforeEmpty, start = False, 0
    for i in range(len(rooms[name])):

        if not isBeforeEmpty:
            if rooms[name][i] == False:
                isBeforeEmpty, start = True, i
            continue
        else:
            if rooms[name][i] == True:
                isBeforeEmpty = False
                emps.append('%02d'%(start+9) + '-'+ '%02d'%(i+9))

    if isBeforeEmpty:
        emps.append('%02d'%(start+9) + '-'+ '18')
    

    print('Room', name+':')
    print('%d available:'%len(emps) if len(emps) else 'Not available')
    if emps:
        print(*emps, sep='\n')
    if name != names[-1]:
        print('-----')