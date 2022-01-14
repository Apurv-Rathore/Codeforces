#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
#define br cout<<endl
#define vi vector<int>
using namespace std;
void solve(){
	int n,k,x;
    cin>>n>>k>>x;
    string s;
    cin>>s;
    vector<int> ans;
    for (int i=0;i<n;i++){
        if (i>0 && s[i-1]=='*' && s[i]=='*'){
            ans[ans.size()-1]+=k;
        }
        else{
            if (s[i]=='*') ans.push_back(k);
        }
    }
    reverse(ans.begin(),ans.end());
    string temp;
    for (auto i:s){
        if (temp=="" || i=='a'){
            temp+=i;
        }
        else if (i=='*' && temp[temp.size()-1]!='*') {
            temp+='*';
        }
    }
    // cout<<temp<<endl;
    s = temp;
    vector<int> res;
    int x1 = x-1;
    for (int i=0;i<ans.size();i++){
        res.push_back(x1%(ans[i]+1));
        x1 = (x1)/(ans[i]+1);
    }
    int ptr = 0;
    string neww;
    int xx = 0;
    for (auto i:temp) {
        if (i=='*') xx++;
    }
    if (res.size()<xx){
        for (int i=0;i<xx-res.size();i++){
            res.push_back(0);
        }
    }
    reverse(res.begin(),res.end());
    for (int i=0;i<temp.size();i++){
        if (temp[i]=='a'){
            neww+='a';
        }
        else{
            if (ptr<res.size()){
                for (int j=0;j<res[ptr];j++){
                    neww+='b';
                }
                ptr++;
            }
        }
    }
    cout<<neww<<endl;



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
