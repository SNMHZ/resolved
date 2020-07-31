#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int solution(vector<int> citations) {
    int answer = 0;
    
    sort(citations.begin(), citations.end(), greater<int>());
    
    while(citations.back()==0)
        citations.pop_back();
    
    for(int i=citations.size()-1; i>=0; i--){
        if(i+1<=citations[i]){
            answer=i+1;
            break;
        }
    }
    
    return answer;
}