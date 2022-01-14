#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
	int n;
    cin>>n;
    int a[n];
    rep(i,n) cin>>a[i];
    vi minn(1025,1e9);
    vi pos(1025,0);
    rep(i,n){
        minn[a[i]] = min(minn[a[i]],a[i]);
        pos[a[i]]=1;
        rep(x,1025){
            if (pos[x]==1){
                if (minn[x]<a[i]){
                    minn[x^a[i]] = min(minn[x^a[i]] , a[i]);
                    pos[x^a[i]]=1;
                }
            }
        }
    }
    int ans = 0;
    vi res;
    res.push_back(0);
    repx(i,1,1025){
        if (pos[i]) {
            ans++;
            res.push_back(i);
        }
        
    }
    // unique(res.begin(),res.end());
    cout<<res.size()<<endl;
    for (auto i:res) cout<<i<<" ";
    br;

}   

signed main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fastio
    int t;
    t = 1;
    // cin>>t;
    while(t--){
		solve();
	}
}
