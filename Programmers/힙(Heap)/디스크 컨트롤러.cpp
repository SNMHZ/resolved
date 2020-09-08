//https://programmers.co.kr/learn/courses/30/lessons/42627

#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> jobs) {
    int answer = 0;
    int current_time=0;
    vector<int> finished;
    
    while(finished.size()!=jobs.size()){
        int index=-1;
        for(int i=0; i<jobs.size(); i++){
            if(jobs[i].size()!=3&&jobs[i][0]<=current_time){
                if(index==-1)
                    index=i;
                else if(jobs[index][1]>jobs[i][1])
                    index=i;
            }
        }
        if(index==-1)
            current_time++;
        else{
            current_time+=jobs[index][1];
            jobs[index].push_back(1);

            finished.push_back(current_time-jobs[index][0]);
        }
    }
    
    int sum=0;
    for(auto k:finished)
        sum+=k;
    
    answer=sum/finished.size();
    
    return answer;
}