#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define int long long
#define rep0(i,n) for (int i=0;i<n;i++)
#define repi(i,x,n) for (int i=x;i<n;i++)
using namespace std;

int fun(string s, vector<int> v){
    int n = v.size();
    int ans = 0;

    int y = n/2;
    if (n%2==0) y--;
    int mid = v[y];
    int left = mid;
    int right = mid;
    if (n%2==0) right = v[y+1];
    // for (auto p:v) cout<<p<<" ";
    // cout<<endl;
    n = s.size();
    // cout<<s<<endl;
    ans = right-left-1;
    // cout<<left<<" "<<right<<endl;
    while (left>=0 && right<n){
        if (s[left]==s[right] && s[right]=='_') {
            ans+=2;
            left--;
            right++;
        }
        else if (s[left]==s[right] && s[left]!='_') {
            ans+=2;
            left--;
            right++;
        }
        else if (s[left]=='_') left--;
        else if (s[right]=='_') right++;
        // cout<<left<<" "<<right<<endl;
        // break;
        
    }
    return ans;
}

bool ispal(string x){
    int l = 0;
    int r = x.size()-1;
    while (l<=r){
        if (x[l]!=x[r]){
            return false;
        }
        l++;
        r--;
    }
    return true;
}
void solve(){
    int n;
    cin>>n;
    string s;
    cin>>s;
    int ans = 0;
    int f = 0;
    rep0(i,26){
        string news;
        string temp;
        vector<int> v;
        string x;
        rep0(j,n){
            // cout<<s[j] - '0'<<" "<<i<<endl;
            if (s[j] - 'a' != i){
                news += s[j];
                v.push_back(j);
                x+=s[j];
            }
            else news += '_';
        }
        if (ispal(x)==false) continue;
        f = 1;
        // cout<<x<<endl;
        ans = max(ans , fun(news,v));
    }
    if (f==0){
        cout<<-1<<endl;
        return;
    }
    cout<<n-ans<<endl;

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
