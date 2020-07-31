def solution(genres, plays):
    answer = []
    gen_dict={}
    gen_count=[]
    
    i=0
    for genre in genres:
        if genre not in gen_dict:
            gen_dict[genre]=[]
            gen_dict[genre].append(plays[i])
            gen_dict[genre].append((plays[i], i))
        else:
            gen_dict[genre][0]+=plays[i]
            gen_dict[genre].append((plays[i], i))
        i+=1
    
    for key in gen_dict.keys():
        gen_count.append((gen_dict[key][0], key))
        del gen_dict[key][0]
        gen_dict[key].sort(key=lambda x:x[0], reverse=True)
    
    gen_count.sort(key=lambda x:x[0], reverse=True)
    
    for key in gen_count:
        flag=0
        for playedtime__index in gen_dict[key[1]]:
            answer.append(playedtime__index[1])
            if flag==1:
                break
            flag=1
    
    return answer