import sys

m12, m3 = sys.stdin.readline().strip().split('=')
m1, m2 = m12.split('+')

chg = {'C':0, 'H':1, 'O':2}
def cnt_atoms(m) -> list:
    res = [0]*3
    before = None
    for w in m:
        if w in ['C', 'H', 'O']:
            res[chg[w]] += 1
            before = w
        else:
            res[chg[before]] += int(w)-1
    return res

m1 = cnt_atoms(m1)
m2 = cnt_atoms(m2)
m3 = cnt_atoms(m3)

for x in range(1, 11):
    for y in range(1, 11):
        for z in range(1, 11):
            if m1[0]*x + m2[0]*y == m3[0]*z:
                if m1[1]*x + m2[1]*y == m3[1]*z:
                    if m1[2]*x + m2[2]*y == m3[2]*z:
                        print(x, y, z)
                        sys.exit(0)
print('NEMOGUCE')