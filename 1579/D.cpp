#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(int t){
	priority_queue<pair<int,int>> g ;
    int n;
    cin>>n;
    int a[n];
    rep0(i,n) cin>>a[i];
    rep0(i,n) g.push({a[i],i});
    int res = 0;
    vector<pair<int,int>> res1;

    while (g.empty()==false){
        int a = g.top().first;
        int i1 = g.top().second;
        if (a==0) break;
        g.pop();
        if (g.empty()) break;
        int b = g.top().first;
        int i2 = g.top().second;
        if (b==0) break;
        g.pop();
        res+=1;
        a-=1;
        b-=1;
        g.push({a,i1});
        g.push({b,i2});
        res1.push_back({i1+1,i2+1});
    }
    cout<<res<<endl;
    for (auto x:res1) cout<<x.first<<" "<<x.second<<endl;
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
		solve(t);
	}
}
