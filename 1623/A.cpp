#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

void solve(){
    int n,m,rb,cb,rd,cd;
    cin>>n>>m>>rb>>cb>>rd>>cd;
    int res = n+m;
    if (rb>rd){
        res = min(res,n-rb+n-rd);
    }
    else{
        res = min(res , rd-rb);
    }
    if (cb>cd){
        res = min(res,m-cb+m-cd);
    }
    else{
        res = min(res , cd-cb);
    }
    cout<<res;
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
    cin>>t;
    while(t--){
		solve();
	}
}
