//https://programmers.co.kr/learn/courses/30/lessons/42842

#include <string>
#include <vector>

using namespace std;

vector<vector<int>> get_expects(int size){
    vector<vector<int>> expects;
    for(int i=1; i<size/2; i++){
        if(!(size%i)){
            if(size/i<i)
                break;
            expects.push_back(vector<int>({size/i, i}));
        }    
    }
    return expects;
}

vector<int> solution(int brown, int yellow) {
    vector<int> answer;
    vector<vector<int>> expects=get_expects(brown+yellow);
    
    for(auto k:expects){
        if( (k[0]-2)*(k[1]-2)==yellow ){
            answer.assign(k.begin(), k.end());
            break;
        }
    }
    
    return answer;
}