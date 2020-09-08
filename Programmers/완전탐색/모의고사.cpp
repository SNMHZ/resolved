//https://programmers.co.kr/learn/courses/30/lessons/42840

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer, correct(3, 0);
    vector<vector<int>> p={ vector<int>({1, 2, 3, 4, 5}), vector<int>({2, 1, 2, 3, 2, 4, 2, 5}), vector<int>({3, 3, 1, 1, 2, 2, 4, 4, 5, 5}) };
    
    for(int i=0; i<p.size(); i++){
        auto itr=p[i].begin();
        for(auto k:answers){
            if(itr==p[i].end())
                itr=p[i].begin();
            if(k==*(itr++))
                correct[i]++;
        }
    }
    
    answer.push_back(1);
    for(int i=1; i<correct.size(); i++){
        if(correct[answer.back()-1]<correct[i]){
            answer.clear();
            answer.push_back(i+1);
        }
        else if(correct[answer.back()-1]==correct[i]){
            answer.push_back(i+1);
        }
    }
    
    return answer;
}