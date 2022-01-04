#include <iostream>
using namespace std;
int main() {
    long long a = 99999999999;
    float b = 99999999999;
    long long c = 99999999998;
    if (a==b){
        cout << "a==b true" << endl;
    }
    if (b==c){
        cout << "b==c true" << endl;
    }
    if (c!=a){
        cout << "c!=a true" << endl;
    }

    if (a == b && b == c && c != a) {
        cout << "true" << '\n';
    } else {
        cout << "false" << '\n';
    }
    return 0;
}