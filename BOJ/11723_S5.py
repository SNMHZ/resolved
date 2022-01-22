import sys

M = int(sys.stdin.readline())

_set = set()
x = None

for _ in range(M):
    oper = sys.stdin.readline().split()
    op = oper[0]

    if op not in ['all', 'empty']:
        x = int(oper[1])

    if op == 'add':
        _set.add(x)
    elif op == 'remove':
        _set.discard(x)
    elif op == 'check':
        print(1 if x in _set else 0)
    elif op == 'toggle':
        _set.discard(x) if x in _set else _set.add(x)
    elif op == 'all':
        del _set
        _set = set(range(1, 21))
    elif op == 'empty':
        del _set
        _set = set()

    del oper