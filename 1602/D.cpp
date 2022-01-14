#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
using namespace std;
void solve(){
    int n;
    cin>>n;
    int a[n+1];
    int b[n+1];
    a[0] = 0;
    b[0] = 0;
    repi(i,1,n+1) cin>>a[i];
    repi(i,1,n+1) cin>>b[i];
    repi(i,1,n+1){
        a[i] = i - a[i];
        b[i]+=i;
    }
    set<int> s;
    rep0(i,n+1) s.insert(i);
    queue<int> q;
    q.push(n);
    int par[n+1];
    rep0(i,n+1) par[i] = -1;
    while(!q.empty()){
        int jumped_to = q.front();
        q.pop();
        int slide_to = b[jumped_to];
        int up = a[slide_to];
        int down = slide_to;
        int val =  *(s.lower_bound(up));
        // cout<<jumped_to<<" "<<up<<" "<<down<<endl;
        while (!s.empty() && val<=down && s.lower_bound(up)!=s.end()){
            q.push(val);
            s.erase((s.lower_bound(up)));
            par[val] = jumped_to;
            // cout<<"val himped "<<val<<" "<<jumped_to<<endl;
            if (s.empty() || s.lower_bound(up)==s.end())  break;
            val =  *(s.lower_bound(up));
        }
    }
    // rep0(i,n+1) cout<<par[i]<<" ";
    // cout<<endl;
    if (par[0]==-1){
        cout<<-1<<endl;
        return;
    }
    int cur = 0;
    vector<int> path;
    while (cur!=n){
        path.push_back(cur);
        cur = par[cur];
    }
    reverse(path.begin(),path.end());
    cout<<path.size()<<endl;
    for (auto p:path) cout<<p<<" ";
    cout<<endl;
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
