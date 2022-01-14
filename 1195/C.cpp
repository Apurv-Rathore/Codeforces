#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define ll long long int
using namespace std;
void solve(){
	int n;
	cin>>n;
	vector<vector<ll>> h(2,vector<ll> (n+1,0));
	vector<vector<ll>> dp(3,vector<ll> (n+1,0));
	for (int i=0;i<n;i++) cin>>h[0][i];
	for (int i=0;i<n;i++) cin>>h[1][i];
	for (int i=1;i<n+1;i++){
		dp[0][i] = max(dp[1][i-1],dp[2][i-1]) + h[0][i-1];
		dp[1][i] = max(dp[0][i-1],dp[2][i-1]) + h[1][i-1];
		dp[2][i] = max(dp[0][i-1],dp[1][i-1]);
	}
	cout<<max(dp[0][n],max(dp[1][n],dp[2][n]))<<endl;
}

signed main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fastio
    int t;
    t = 1;
    // cin>>t;
    while(t--){
		solve();
	}
}
