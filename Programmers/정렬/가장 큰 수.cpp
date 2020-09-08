//https://programmers.co.kr/learn/courses/30/lessons/42746

#include <string>
#include <vector>
#include <algorithm>

using namespace std;

bool cmp(const string &p1, const string &p2){
    string temp1=p1+p2;
    string temp2=p2+p1;
      
    if(temp1.length()!=temp2.length())
        if(temp1.length()<temp2.length())
            return false;
        else
            return true;
    
    for(int i=0; i<temp1.length(); i++){
        if(temp1[i]>temp2[i])
            return true;
        else if(temp1[i]==temp2[i])
            continue;
        else if(temp1[i]<temp2[i])
            return false;
    }

    return false;
}

string solution(vector<int> numbers) {
    string answer = "";
    vector<string> numstr;
    for(int i=0; i<numbers.size(); i++)
        numstr.push_back(to_string(numbers.at(i)));
    
    sort(numstr.begin(), numstr.end(), cmp);
    
    for(int i=0; i<numstr.size(); i++)
        answer+=numstr[i];
    
    if(answer[0]=='0')
        answer="0";
    
    return answer;
}