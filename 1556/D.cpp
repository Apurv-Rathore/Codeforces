#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for(int i=0;i<n;i++)
#define onerep(i,n) for(int i=1;i<n;i++)
using namespace std;

int ask(int i, int j){
	cout<<"and "<<i+1<<" "<<j+1<<endl;
	fflush(stdout);
	int andd;
	cin>>andd;
	cout<<"or "<<i+1<<" "<<j+1<<endl;
	fflush(stdout);
	int orr;
	cin>>orr;
	return andd + orr;
}

void solve(){
	int n,k;
	cin>>n>>k;
	int sum[n-1];
	rep(i,n-1){
		sum[i] = ask(i,i+1);
	}
	n = n-1;
	int dif = 0;
	rep(i,n-abs(n%2)){
		dif = sum[i] - dif;
	}
	int end = n - n%2 ;
	int first = 0;
	int firstelement = (ask(first,end) + dif)/2;
	firstelement -= dif;
	// cout<<"firstelement "<<firstelement<<endl;
	// cout<<"dif "<<dif<<endl;
	vector<int> res;
	res.push_back(firstelement);
	rep(i,n){
		res.push_back(sum[i] - firstelement);
		firstelement = sum[i] - firstelement;
	}
	// rep(i,res.size()) cout<<res[i]<<" ";
	// cout<<endl;
	sort(res.begin(),res.end());
	cout<<"finish "<<res[k-1]<<endl;;


}

signed main(){
    // #ifndef ONLINE_JUDGE
    //     freopen("input.txt", "r", stdin);
    //     freopen("output.txt", "w", stdout);
    // #endif
    // fastio
    int t;
    t = 1;
    // cin>>t;
	
    while(t--){
		solve();
	}
}
