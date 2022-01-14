#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

void solve(){
    // number of increasing is >=n 
    // 2n! - # of bad 
    int n;
    cin>>n;
    int res = 1;
    repx(i,3,2*n+1) {
        res = res * i ;
        res %= 1000000007;
    }
    // res = res/2;
    cout<<res<<endl;

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
    while(t--){
		solve();
	}
}
