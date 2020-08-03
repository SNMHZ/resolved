#include <string>
#include <vector>
#include <queue>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int answer = 0;
    
    queue<int> bridge;
    for(int i=0; i<bridge_length; i++)
        bridge.push(0);
    
    int time=0, current_weight=0;
    while(!bridge.empty()){
        time++;
        
        current_weight-=bridge.front();
        bridge.pop();
        
        if(!truck_weights.empty()){
            if(current_weight+truck_weights.back()<=weight){
                current_weight+=truck_weights.back();
                bridge.push(truck_weights.back());
                truck_weights.pop_back();
            }
            else
                bridge.push(0);
        }
    }
    
    answer=time;
    
    return answer;
}