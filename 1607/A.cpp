#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

void solve(){
    string s;
    cin>>s;
    int n = s.size();
    map<char,int> m;
    rep(i,n){
        m[s[i]] = i;
    }
    string t;
    cin>>t;
    int ans = 0;
    int prev = m[t[0]];
    repx(i,1,t.size()){
        ans += abs(prev - m[t[i]]);
        prev = m[t[i]];
    }
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
