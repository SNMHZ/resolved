#https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    answer = 1
    clothe_dict={}
    
    for cloth in clothes:
        if cloth[1] not in clothe_dict:
            clothe_dict[cloth[1]]=[]
            clothe_dict[cloth[1]].append(cloth[0])
        else:
            clothe_dict[cloth[1]].append(cloth[0])
    
    for gen in clothe_dict.keys():
        answer*=(len(clothe_dict[gen])+1)
    
    return answer-1