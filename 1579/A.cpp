#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repx(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
	string s;
    cin>>s;
    int a=0;
    int b=0;
    int c=0;
    rep0(i,s.size()){
        if (s[i]=='A') a++;
        else if (s[i]=='B') b++;
        else c++;
    }
    // 3 2 1 
    int ok = 0;
    rep0(x,50){
        rep0(y,50){
            if (a==x and (b==x+y) and (c==y)) {
                ok = 1;
            }

        }
    }
    if (ok) cout<<"YES";
    else cout<<"NO";
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
    cin>>t;
    while(t--){
		solve();
	}
}
