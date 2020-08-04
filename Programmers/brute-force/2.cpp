#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void dfs_subnum(string str, string sub, int n, vector<int> *subnums, vector<bool> check){
    check[n]=true;
    vector<bool> check2;
    check2.assign(check.begin(), check.end());
    subnums->push_back(stoi(sub));
    
    for(int i=0; i<str.size(); i++){
        if(check[i]==true)
            continue;
        dfs_subnum(str, sub+str.substr(i, 1), i, subnums, check2);
    }
}

bool prime_checker(int n, vector<int> *primes){
    if(n==1) return false;
    if(n==2) return true;
    for(int i=2; i<n; i++)
        if(!(n%i)) return false;
    return true;
}

int solution(string numbers) {
    int answer = 0;
    vector<int> primes, subnums;
    vector<bool> check(numbers.size(), false);
    
    for(int i=0; i<numbers.size(); i++){
        check.clear();
        subnums.clear();
        check.assign(numbers.size(), false);
        dfs_subnum(numbers, numbers.substr(i, 1), i, &subnums, check);
        for(auto k:subnums)
            if(prime_checker(k, &primes))
                primes.push_back(k);
    }
    
    sort(primes.begin(), primes.end());
    int tmp=0;
    for(auto k:primes)
        if(k!=tmp){
            answer++;
            tmp=k;
        }

    return answer;
}