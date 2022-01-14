#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
using namespace std;
void solve(){
	int n,H;
    cin>>n>>H;
    vector<int> a(n,0);
    for (int i=0;i<n;i++) cin>>a[i];
    sort(a.begin(),a.end());
    int aa = a[n-1] + a[n-2];
    int cnt = (H/aa)*2;
    // cout<<H<<" "<<cnt<<endl;
    if (H%aa>0){
        if (H%aa>a[n-1])cnt+=2;
        else cnt++;
    }
    cout<<cnt<<endl;
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
