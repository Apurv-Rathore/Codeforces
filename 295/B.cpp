#include <bits/stdc++.h>
#define int long long
#define rep(i,n) for(int i=0;i<n;i++)
#define onerep(i,n) for(int i=1;i<n;i++)
using namespace std;

 
signed main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    int n;
	cin>>n;
	int dp[n][n];
	int mat[n][n];
	rep(i,n){
		rep(j,n){
			cin>>dp[i][j];
		}
	}
	int x[n];
	rep(i,n) cin>>x[i];
	reverse(x,x+n);
	vector<int> ans;
	vector<int> covered(n,0);
	
	rep(l,n){
		int k = x[l]-1;
		rep(i,n){
			rep(j,n){
				dp[i][j] = min(dp[i][j] , dp[i][k]+dp[k][j]);
			}
		}
		covered[k]=1;
		int res = 0;
		rep(i,n){
			rep(j,n){
				if (covered[i]&&covered[j]) res+=dp[i][j];
			}
		}
		ans.push_back(res);


	}
	reverse(ans.begin(),ans.end());
	rep(i,n) cout<<ans[i]<<" ";
}