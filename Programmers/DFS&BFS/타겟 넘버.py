#https://programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

class Node:
    def __init__(self, _depth, _current):
        self.depth = _depth
        self.current = _current

def dfs(numbers, target):
    answer = 0
    open_list = deque()
    
    open_list.append( Node(1, numbers[0]) )
    open_list.append( Node(1, -numbers[0]) )
    
    while open_list:
        current_node = open_list.pop()
        
        if current_node.depth < len(numbers):
            open_list.append( Node(current_node.depth + 1, current_node.current + numbers[current_node.depth]) )
            open_list.append( Node(current_node.depth + 1, current_node.current - numbers[current_node.depth]) )
        else:
            if current_node.current == target:
                answer += 1
    return answer

def bfs(numbers, target):
    answer = 0
    open_list = deque()
    
    open_list.append( Node(1, numbers[0]) )
    open_list.append( Node(1, -numbers[0]) )
    
    while open_list:
        current_node = open_list.popleft()
        
        if current_node.depth < len(numbers):
            open_list.append( Node(current_node.depth + 1, current_node.current + numbers[current_node.depth]) )
            open_list.append( Node(current_node.depth + 1, current_node.current - numbers[current_node.depth]) )
        else:
            if current_node.current == target:
                answer += 1
    return answer

def solution(numbers, target):
    return dfs(numbers, target) #bfs(numbers, target)