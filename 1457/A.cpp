#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define ll long long
using namespace std;

int dis(int x, int y, int r, int c){
    return abs(x-r)+abs(y-c);
}

int main(){
    fastio
    int t;
    t = 1;
    cin>>t;
    while(t--){
        // int n;
        // cin>>n;
        int n,m,r,c;
        cin>>n>>m>>r>>c;
        int ans = 0;
        ans=max(ans,dis(r,c,1,1));
        ans=max(ans,dis(r,c,1,m));
        ans=max(ans,dis(r,c,n,1));
        ans=max(ans,dis(r,c,n,m));
        cout<<ans<<endl;
    }
}