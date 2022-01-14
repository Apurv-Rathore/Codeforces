#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
	int n,k;
    cin>>n>>k;
    if ((n+abs(n%2))/2<k){
        cout<<-1<<endl;
        return;
    }
    int pos = 0;
    int f = 0;
    rep(i,n){
        rep(j,n){
            if (j==pos && k>0 && f==0) {
                cout<<"R";
                k--;
            }
            else cout<<".";
        }
        if (f==0) f=1;
        else f=0;
        cout<<endl;
        pos++;
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
    cin>>t;
    while(t--){
		solve();
	}
}
