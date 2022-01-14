#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define ll long long int
using namespace std;
void solve(){
	vector<string> arr(2,"");
	cin>>arr[0];
	cin>>arr[1];
	int n = arr[0].size();
	int ans = 0;
	if (n==0) {
		cout<<0<<endl;
		return;
	}
	if (arr[0][0]=='0' && arr[1][0]=='0'){
		if (arr[0][1]=='0'){
			arr[0][1]='X';
			arr[0][0]='X';
			arr[1][0]='X';
			ans++;
		}
		else if (arr[1][1]=='0'){
			arr[1][1]='X';
			arr[0][0]='X';
			arr[1][0]='X';
			ans++;
		}
	}
	for (int i=1;i<n;i++){
		// cout<<arr[0]<<endl;
		// cout<<arr[1]<<endl;
		if (arr[0][i]=='0' && arr[1][i]=='0'){
			if (arr[0][i-1]=='0'){
				ans++;
				arr[0][i-1]='X';
				arr[0][i]='X';
				arr[1][i]='X';
			}
			else if (arr[1][i-1]=='0'){
				ans++;
				arr[1][i-1]='X';
				arr[0][i]='X';
				arr[1][i]='X';
			}
			else if (arr[0][i+1]=='0'){
				ans++;
				arr[0][i+1]='X';
				arr[0][i]='X';
				arr[1][i]='X';
			}
			else if (arr[1][i+1]=='0'){
				ans++;
				arr[1][i+1]='X';
				arr[0][i]='X';
				arr[1][i]='X';
			}
		}
		if (i<n-1 && ( arr[0][i]=='0' || arr[1][i]=='0')){
			if (arr[0][i+1]=='0' && arr[1][i+1]=='0'){
				arr[0][i]='X';
				arr[1][i]='X';
				arr[0][i+1]='X';
				arr[1][i+1]='X';
				ans++;
			}
			else if (arr[0][i-1]=='0' && arr[1][i-1]=='0' && (arr[0][i]=='0' || arr[1][i]=='0')){
				arr[0][i]='X';
				arr[1][i]='X';
				arr[0][i-1]='X';
				arr[1][i-1]='X';
				ans++;
			}
		}
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
    // cin>>t;
    while(t--){
		solve();
	}
}
