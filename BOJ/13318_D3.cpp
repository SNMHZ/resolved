#include<stdio.h>
#include<iostream>
#include<string>
#include<algorithm>
#include<cassert>
#include<stdlib.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> pll;

const int MM = 1000000007;

string A, B;

int DB[31] = {29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79};

int main()
{
	cin >> A >> B;
	assert(A.size() <= 300000 && B.size() <= 300000 && A != B && A.size() == B.size());
	for(char c : A){
		assert( 'a' <= c && c <= 'z');
	}
	for(char c : B){
		assert( 'a' <= c && c <= 'z');
	}

	for(int i = 0; i < 10; i++){
		ll p = DB[i], q = 1, r = 0, s = 0;
		for(char a : A){
			r = (r + q * a) % MM;
			q = p*q % MM;
		}
		q = 1;
		for(char b : B){
			s = (s + q * b) % MM;
			q = p*q % MM;
		}
		assert( r == s );
	}
	return 0;
}
