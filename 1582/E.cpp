#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

int dp[100001][448];
void solve(){
    int n;
    cin>>n;
    int a[n];
    rep(i,n) cin>>a[i];
    rep(i,n){
        rep(j,448) dp[i][j] = -1e18;
    }
    reverse(a,a+n);
    int pre[n];
    pre[0] = a[0];
    repx(i,1,n) pre[i] = pre[i-1] + a[i];
    // so dp[i][j] = till suffix [0...i] and choosen segments with length j,j-1,..1 
    rep(i,n){
        repx(j,1,448){
            if (i==0){
                if (j==1) dp[i][j] = a[i];
            }
            else{
                if (j==1){
                    dp[i][j] = max(dp[i-1][j] , a[i]);
                }
                else{
                    if (j<=i){
                        // try to take i into this segment
                        int thissum = pre[i] - pre[i-j];
                        if (thissum < dp[i-j][j-1]){
                            dp[i][j] = thissum;
                        }
                        // if (i==2 && j==2){
                        //     cout<<"f"<<thissum<<" ";
                        // }
                        dp[i][j] = max(dp[i][j] , dp[i-1][j]);
                    }
                }
            }
            // cout<<dp[i][j]<<" ";
        }
        // br;
        
    }
    int res = 0;
    int k = 0;
    repx(i,1,448) {
        if (dp[n-1][i]>0){
            res = dp[n-1][i];
            k = i;
        }
    }
    cout<<k<<endl;
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
