import sys

N = int(sys.stdin.readline())
datas = [list(sys.stdin.readline().split()[1:]) for _ in range(N)]
graph = {}

for data in datas:
    cur = ''
    for i in range(len(data)-1):
        cur += data[i]+' '
        graph[cur] = graph.get(cur, [])+[cur+data[i+1]+' ']

st = sorted(list(set([d[0]+' ' for d in datas])), reverse=True)
while st:
    cur = st.pop()
    e = cur.split(' ')[-2]
    i = len(cur.split(' '))-2
    print(('--'*int(i))+e)
    st += sorted( list(set(graph.get(cur, []))), reverse=True)