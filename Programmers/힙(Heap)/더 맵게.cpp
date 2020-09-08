//https://programmers.co.kr/learn/courses/30/lessons/42626

#include <string>
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

int solution(vector<int> scoville, int K) {
    int answer = 0;
    int temp;

    make_heap(scoville.begin(), scoville.end(), greater<int>());
    
    while(scoville[0]<K){
        if(scoville.size()==1){
            answer=-1;
            break;
        }
        pop_heap(scoville.begin(), scoville.end(), greater<int>());
        temp=scoville.back();
        scoville.pop_back();
        pop_heap(scoville.begin(), scoville.end(), greater<int>());
        scoville.back()=scoville.back()*2+temp;
        push_heap(scoville.begin(), scoville.end(), greater<int>());
        answer++;
    }
    
    return answer;
}
