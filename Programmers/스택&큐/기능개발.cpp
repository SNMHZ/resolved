//https://programmers.co.kr/learn/courses/30/lessons/42586

#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> end;
    
    for(int i=0; i<progresses.size(); i++){
        end.push_back((100-progresses[i])/speeds[i]);
        if((100-progresses[i])%speeds[i]!=0)
            end.back()++;
    }
    
    int i, index=0;
    for(i=1; i<end.size(); i++){
        if(end[i]>end[index]){
            answer.push_back(i-index);
            index=i;
        }
    }
    if(end.size())
        answer.push_back(i-index);
    
    return answer;
}