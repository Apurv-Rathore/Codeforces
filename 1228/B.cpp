
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
ll mod=1e9+7,ans=1;
ll c[1009],r[1009];
int main()
{
 
ll w,h;
cin>>h>>w;
for(int i=1;i<=h;i++)cin>>r[i];
for(ll i=1;i<=w;i++)cin>>c[i];
for(int i=1;i<=h;i++)
    for(ll j=1;j<=w;j++)
{
    if((i-1)==c[j]&&(j-1)<r[i]){cout<<0;return 0;}
    if((j-1)==r[i]&&(i-1)<c[j]){cout<<0;return 0;}
     if(((i-1)>c[j])&&(j-1)>r[i])ans=(ans*2)%mod;
}
cout<<ans;
    return 0;
}