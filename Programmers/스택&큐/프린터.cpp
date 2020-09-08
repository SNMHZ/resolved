//https://programmers.co.kr/learn/courses/30/lessons/42587

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int solution(vector<int> priorities, int location) {
    int answer = 0;
    vector<int> priorities_sorted;
    vector<int> _printed;
    
    //copy & sort priorities
    priorities_sorted.assign(priorities.begin(), priorities.end());
    sort(priorities_sorted.begin(), priorities_sorted.end());
    

    auto iter=priorities.begin();
    while(_printed.size()!=priorities.size()){
        if(iter==priorities.end())
            iter=priorities.begin();
        
        if(*iter==priorities_sorted.back()){
            _printed.push_back(iter-priorities.begin());
            priorities_sorted.pop_back();
            
            if(_printed.back()==location)
                return answer=_printed.size();
        }
        
        iter++;
    }
    
    /*
    for(int i=0; i<_printed.size(); i++){
        if(_printed[i]==location){
            answer=i+1;
            break;
        }
    }*/
    
    //return answer;
}