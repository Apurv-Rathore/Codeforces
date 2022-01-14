#include <iostream>
#define MOD 1000000007

using namespace std;

int dp[105][2];

int main()
{
    int i,j,n,k,d;
    cin>>n>>k>>d;
    dp[0][0]=1;
    if(d==1)
        dp[1][1]=1;
    else
        dp[1][0]=1;
    for(i=2;i<=n;++i)
    {
        for(j=1;j<d && j<=i;++j)
            dp[i][0]=(dp[i][0]+dp[i-j][0])%MOD;
        for(j=1;j<d && j<=i;++j)
            dp[i][1]=(dp[i][1]+dp[i-j][1])%MOD;
        for(j=d;j<=k && j<=i;++j)
            dp[i][1]=(1LL*dp[i][1]+dp[i-j][0]+dp[i-j][1])%MOD;
    }
    cout<<dp[n][1];
    return 0;
}
