#include <bits/stdc++.h>
#define MOD 1000000007
#define Nmax 1000005
#define pb push_back
#define mp make_pair
#define INF (1LL<<62)
#define eps 0.000000000001

using namespace std;

int n,m,a[Nmax];
long long dp[Nmax][20],Cost[50][50];

inline int Biti(int x)
{
    int sol=0;
    while(x)
    {
        ++sol; x=(x&(x-1));
    }
    return sol;
}

int main()
{
    int i,j,k,x,y,c;
    long long sol=-INF;
    #ifndef ONLINE_JUDGE
        freopen ("date.in","r",stdin);
        freopen ("date.out","w",stdout);
    #endif
    cin.sync_with_stdio(0);
    cin>>n>>m>>k;
    for(i=1;i<=n;++i) cin>>a[i];
    while(k--)
    {
        cin>>x>>y>>c;
        Cost[x][y]+=c;
    }
    int lim=(1<<n)-1;
    for(i=0;i<=lim;++i)
        for(j=0;j<=n;++j) dp[i][j]=-INF;
    dp[0][0]=0;
    for(i=0;i<=lim;++i)
    for(j=0;j<=n;++j)
    {
        if(dp[i][j]==-INF) continue;
        for(k=0;k<n;++k)
            if(((1<<k)&i)==0)
            {
                dp[i+(1<<k)][k+1]=max(dp[i+(1<<k)][k+1],dp[i][j]+a[k+1]+Cost[j][k+1]);
            }
    }
    for(i=0;i<=lim;++i)
        for(j=1;j<=n;++j)
        if(Biti(i)==m) sol=max(sol,dp[i][j]);
    cout<<sol;
    return 0;
}
