#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
using namespace std;
int power(int x,  int y, int p)
{
    int res = 1;     // Initialize result
 
    x = x % p; // Update x if it is more than or
                // equal to p
  
    if (x == 0) return 0; // In case x is divisible by p;
 
    while (y > 0)
    {
        // If y is odd, multiply x with result
        if (y & 1)
            res = (res*x) % p;
 
        // y must be even now
        y = y>>1; // y = y/2
        x = (x*x) % p;
    }
    return res;
}

void solve(){
    int n,k;
    cin>>n>>k;
    string b;
    while (k>0){
        if (k%2){
            b+='1';
        }
        else{
            b+='0';
        }
        k/=2;
    }
    int ans = 0;
    int mod = (int)1e9+7;
    for (int i=0;i<b.size();i++){
        if (b[i]=='1') ans += power(n,i,mod); 
        ans%=mod;
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




