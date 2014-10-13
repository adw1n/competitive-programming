#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstring>
#include <set>
#include <numeric> //accumulate(i poczatek,i koniec, wartosc_poczatkowa)
#include <utility> //swap
#include <map>
#include <cmath>

using namespace std;

typedef vector<int> VI;
typedef long long LL;

#define FOR(x, b, e) for(int x = b; x <= (e); ++x)
#define FORD(x, b, e) for(int x = b; x >= (e); --x)
#define REP(x, n) for(int x = 0; x < (n); ++x)
#define VAR(v, n) __typeof(n) v = (n)
#define ALL(c) (c).begin(), (c).end()
#define SIZE(x) ((int)(x).size())
#define FOREACH(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define PB push_back
#define ST first
#define ND second
#define MP make_pair

//http://acm.tju.edu.cn/toj/showp1007.html 1007.   Joseph
int main (int argc, char * const argv[]) {
	
	ios_base::sync_with_stdio(0);
	int k;
	while(cin>>k){
	if(k==0) break;
	switch(k){
		case 1:
		cout<<2;
		break;
		case 2:
		cout<<7;
		break;
		case 3:
		cout<<5;
		break;
		case 4:
		cout<<30;
		break;
		case 5:
		cout<<169;
		break;
		case 6:
		cout<<441;
		break;
		case 7:
		cout<<1872;
		break;
		case 8:
		cout<<7632;
		break;
		case 9:
		cout<<1740;
		break;
		case 10:
		cout<<93313;
		break;
		case 11:
		cout<<459901;
		break;
		case 12:
		cout<<1358657;
		break;
		case 13:
		cout<<2504881;
		break;
	}
	cout<<endl;
	//k == num of good guys == num of bad guys
	/*
	FOR(ans,k+1,100000000){
	//check if ans is a vaild ans
	//if a guy with number <=k is removed its not valid
	bool possible=1;
	int size=2*k;
	int indexToRemove=ans;
	indexToRemove%=size;
	if(indexToRemove==0)indexToRemove=size;
	REP(x,k){
		//only k removals needed
		//calculate a guy to remove
		if(indexToRemove<=k) {possible=0;break;}
		size--;
	FOR(y,1,ans){
		indexToRemove++;
		if(indexToRemove==size+2) {indexToRemove=1;indexToRemove+=(ans-y)%size;break;}
		}
	}
	if(possible) {cout<<ans<<endl;break;}
	}
	*/
	}
	
    return 0;
}
