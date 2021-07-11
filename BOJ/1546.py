n = input()
inp = [ int(x) for x in input().split() ]

_max = max(inp)

print( sum([ x/_max*100 for x in inp ])/len(inp) )