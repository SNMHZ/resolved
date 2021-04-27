#https://programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0
    to_explore = [x for x in range(n)]
    open_list = []
    
    while to_explore:
        open_list.append( to_explore[0] )
        while open_list:
            current_node = open_list.pop()
            if current_node in to_explore:
                to_explore.remove(current_node)
            for i, child in enumerate(computers[current_node]):
                if (i in to_explore) and (child == 1):
                    open_list.append( i )
        answer +=1

    return answer