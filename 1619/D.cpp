#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
	int n,m;
    cin>>n>>m;
    int l[n][m];
    set<int> mxshop;
    rep(i,n){
        rep(j,m){
            cin>>l[i][j];
        }
    }
    int res = 10000000000;
    rep(j,m){
        int indx = -1;
        int val = 0;
        rep(i,n){
            if (l[i][j]>=val){
                indx = i;
                val = l[i][j];
            }
        }
        
        res = min(res,val);
        mxshop.insert(indx);
    }
    if (mxshop.size()<m){
        cout<<res<<endl;
        return;
    }
    int low = 0;
    int high = 1000000000;
    int ans = 0;
    while (low<=high){
        int mid = (low+high)/2;
        // cout<<mid<<endl;
        int shoptaken[n];
        int greaterreached[m];
        memset(shoptaken,0,sizeof(shoptaken));
        memset(greaterreached,0,sizeof(greaterreached));
        rep(i,n){
            rep(j,m){
                if (l[i][j]>=mid){
                    greaterreached[j]=1;
                    shoptaken[i]+=1;
                }
            }
        }
        if (*max_element(shoptaken,shoptaken+n)>1 && *min_element(greaterreached,greaterreached+m)==1){
            ans = mid;
            low = mid+1;
        }
        else high = mid-1;
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
