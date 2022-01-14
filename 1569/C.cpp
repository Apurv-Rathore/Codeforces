#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
using namespace std;
int mod = 998244353;
int fact(int n, int x, int leave){
    int res = 1;
    repi(i,x,n+1){
        if (i==leave) continue;
        res*=i;
        res%=mod;
    }
    return res;
}
void solve(){
    int n;
    cin>>n;
    int a[n];
    rep0(i,n) cin>>a[i];
    int m = *max_element(a,a+n);
    int mxcnt = count(a,a+n,m);
    if (mxcnt>1){
        int res = fact(n,1,0);
        cout<<res<<endl;
        return;
    }
    int k = count(a,a+n,m-1);
    if (k==0){
        cout<<0<<endl;
        return; 
    }
    int tosub = fact(n,1,k+1);
    int res = (fact(n,1,0) - tosub+mod)%mod;
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
