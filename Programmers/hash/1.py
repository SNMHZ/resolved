def solution(participant, completion):
    answer = ''
    tdict={}
    
    for name in participant:
        if name not in tdict:
            tdict[name]=0
        else:
            tdict[name]+=1
    
    for name in completion:
        if tdict[name]==0:
            tdict.pop(name)
        else:
            tdict[name]-=1
    
    answer=list(tdict.keys())[0]
    return answer