//https://programmers.co.kr/learn/courses/30/lessons/42748

#include <string>
#include <vector>
#include <algorithm>

using namespace std;


int vec_slice_and_get(vector<int> array, vector<int> command){
    vector<int> sliced;
    for(int i=command[0]-1; i<command[1]; i++)
        sliced.push_back(array.at(i));
    sort(sliced.begin(), sliced.end());
    return sliced.at(command[2]-1);
}

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    
    for(int i=0; i<commands.size(); i++)
        answer.push_back(vec_slice_and_get(array, commands.at(i)));
    
    return answer;
}