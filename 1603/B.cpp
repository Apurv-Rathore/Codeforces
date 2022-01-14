#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(int t){
	int x,y;
    cin>>x>>y;
    if (x==y) cout<<x;
    else if (x>y) cout<<x+y;
    else cout<<y - (y%x)/2;
    cout<<endl;
}

signed main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fastio
    int t;
    t = 1;
    cin>>t;
    int c = 0;
    while(t--){
		solve(c);
        c++; 
	}
}
