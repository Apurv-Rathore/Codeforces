#include <bits/stdc++.h>
#define Nmax 505
#define pii pair <int,int>
#define mp make_pair
#define pb push_back
#define fi first
#define se second

using namespace std;

int n,a[Nmax];
bool dp[Nmax][Nmax][Nmax];
vector <int> ans;

int main()
{
    int n,val,i,x,cost,j,k;
    #ifndef ONLINE_JUDGE
        freopen ("date.in","r",stdin);
        freopen ("date.out","w",stdout);
    #endif
    cin>>n>>val;
    for(i=1;i<=n;++i) cin>>a[i];
    dp[0][0][0]=1;
    for(i=1;i<=n;++i)
        for(j=0;j<=val;++j)
            for(k=0;k<=j;++k)
            {
                dp[i][j][k]=dp[i-1][j][k];
                if(a[i]<=j)
                {
                    dp[i][j][k]|=dp[i-1][j-a[i]][k];
                    if(k>=a[i])
                        dp[i][j][k]|=dp[i-1][j-a[i]][k-a[i]];
                }
            }
    for(i=0;i<=val;++i)
        if(dp[n][val][i]) ans.pb(i);
    cout<<ans.size()<<"\n";
    for(auto it : ans) cout<<it<<" ";
    return 0;
}
