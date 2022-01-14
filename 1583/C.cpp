#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
using namespace std;
void solve(){
	int n,m;
    cin>>n>>m;
    vector<string> v;
    rep(i,n){
        string s;
        cin>>s;
        v.push_back(s);
    }
    int a[m];
    memset(a,0,sizeof(a));
    rep(i,n-1){
        rep(j,m-1){
            if (v[i+1][j]==v[i][j+1] && v[i][j+1]=='X'){
                a[j+1]+=1;
            }
        }
    }

    int pre[m];
    pre[0] = a[0];
    repx(i,1,m) {
        pre[i] = pre[i-1] + a[i];
    }
    int q;
    cin>>q;
    while(q--){
        int x1,x2;
        cin>>x1>>x2;
        x1--;
        x2--;
        if (pre[x2]>pre[x1]){
            cout<<"NO";
        }
        else cout<<"YES";
        br;
    }
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
