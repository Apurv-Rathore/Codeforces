#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;

vector<pair<int,int>> g[200001];
set<int> not_taken;
int vis[200001];
void dfs(int n, int p, int bit){
    for(auto c:g[n]){
        if (c.first==p) continue;
        int x = c.second&(1<<bit);
        if ((c.first!=p && x==0 ) && vis[c.first]==0){
            int f = 1;
            for (auto bb:not_taken){
                int xx = c.second&(1<<bb);
                if (xx!=0) f = 0;
            }
            if (!f) continue;
            vis[c.first]=1;
            dfs(c.first,n,bit);
        }
    }
}
void solve(){

    not_taken.clear();
    int n,m,a,b,c;
    cin>>n>>m;
    rep(i,n) g[i].clear();
    rep(i,m){
        cin>>a>>b>>c;
        a--;
        b--;
        g[a].push_back({b,c});
        g[b].push_back({a,c});
    }
    for(int i=30;i>=0;i--){
        rep(j,n) vis[j]=0;
        vis[0]=1;
        dfs(0,-1,i);
        int f = 1;
        rep(j,n){
            if (!vis[j]) f=0;
        }
        if (f==1){
            not_taken.insert(i);
        }
    }
    int res = 0;
    for (int i=0;i<=30;i++){
        if (not_taken.find(i)==not_taken.end()){
            res += 1<<i;
        }
    }
    cout<<res;br;

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
