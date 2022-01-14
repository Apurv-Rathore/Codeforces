#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
using namespace std;
void solve(){
    int n;
    cin>>n;
    int a[n];
    rep0(i,n) cin>>a[i];
    int zero = 0;
    int one = 0;
    rep0(i,n){
        if (a[i]==0) zero++;
        else if (a[i]==1) one++;
    }
    int ans = one * pow(2,zero);
    cout<<ans<<endl;

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
