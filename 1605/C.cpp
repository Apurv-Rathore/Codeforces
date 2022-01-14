#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    for (int i=1;i<n;i++){
        if (s[i]=='a' && s[i-1]=='a'){
            cout<<2<<endl;
            return;
        }
    }
    for (int i=2;i<n;i++){
        if (s[i]=='a' && s[i-2]=='a'){
            cout<<3<<endl;
            return;
        }
    }

    for (int i=3;i<n;i++){
        if (s[i]=='a' && s[i-3]=='a' && s[i-1]!=s[i-2]){
            cout<<4<<endl;
            return;
        }
    }

    if (s.find("abbacca")!=-1 || s.find("accabba")!=-1){
        cout<<7<<endl;
        return;
    }
    cout<<-1<<endl;

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
