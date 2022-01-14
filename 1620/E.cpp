#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

signed main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    // fastio
	int q;
    cin>>q;
    int dp[q][2];
    // return 0;
    
    vector<int> m(500001);
    for (int i=0;i<500001;i++) m[i]=i;
    int cnt=0;
    for (int i=0;i<q;i++){
        int a;
        cin>>a;
        if (a==1){
            int x;
            cin>>x;
            cnt++;
            dp[i][1] = x;
            dp[i][0]=0;
        }
        else{
            cin>>dp[i][0]>>dp[i][1];
        }
    }
    int res[cnt];
    int ptr=cnt-1;;
    for (int i=q-1;i>=0;i--){
        int xx = dp[i][1];
        if (dp[i][0]!=0){
            m[dp[i][0]]=m[xx];
        }
        else{
            res[ptr] = m[xx];
            ptr--;
        }
    }
    for (int i=0;i<cnt;i++){
        cout<<res[i]<<" ";
    }
}
