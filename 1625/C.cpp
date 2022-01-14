#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
#define MAX 100000000000000000
using namespace std;
void solve(){
	int n,l,k;
    cin>>n>>l>>k;
    vi d;
    vi a;
    rep(i,n) {
        int x;
        cin>>x;
        d.push_back(x);
    }
    rep(i,n) {
        int x;
        cin>>x;
        a.push_back(x);
    }
    a.push_back(0);
    d.push_back(l);
    int dp[n+1][k+1];
    rep(i,n+1){
        rep(j,k+1) dp[i][j]=MAX;
    }
    dp[n][0]=0;
    for (int i=n-1;i>=0;i--){
        for (int j=0;j<=k;j++){
            dp[i][j] = min(dp[i+1][j] + (d[i+1]-d[i])*a[i],dp[i][j]);
            for (int r=i+1;r<n;r++){
                if (j + (r-i)>k) break ;
                dp[i][j + (r-i)] = min(dp[r+1][j] + (d[r+1]-d[i])*a[i],dp[i][j+r-i]);
            }
        }
    }
    int res = MAX;
    rep(i,k+1){
        res = min(res , dp[0][i]);
    }
    // res = *min_element(dp[n],dp[n]+k+1);
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
    // cin>>t;
    while(t--){
		solve();
	}
}
