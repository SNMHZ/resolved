//https://programmers.co.kr/learn/courses/30/lessons/42628

#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

vector<int> solution(vector<string> operations) {
    vector<int> answer;
    vector<int> my_heap;
    
    string temp;
    for(int i=0; i<operations.size(); i++){
        if(operations[i][0]=='I'){
            temp=operations[i].substr(2, operations[i].size()-1);
            my_heap.push_back(stoi(temp));
            push_heap(my_heap.begin(), my_heap.end());
        }
        else if(operations[i]=="D 1"){
            if(!my_heap.empty()){
                pop_heap(my_heap.begin(), my_heap.end());
                my_heap.pop_back();
            }
        }
        else{
            if(!my_heap.empty()){
                make_heap(my_heap.begin(), my_heap.end(), greater<int>());
                pop_heap(my_heap.begin(), my_heap.end(), greater<int>());
                my_heap.pop_back();
                make_heap(my_heap.begin(), my_heap.end());
            }
        }
    }
    
    int biggest, smallest;
    if(my_heap.empty())
        biggest=smallest=0;
    else{
        sort_heap(my_heap.begin(), my_heap.end());
        smallest=my_heap.front();
        biggest=my_heap.back();
    }
    answer.push_back(biggest);
    answer.push_back(smallest);
    
    return answer;
}