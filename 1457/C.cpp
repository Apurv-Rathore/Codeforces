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
        int n,p,k,x,y;
        string s;
        cin>>n>>p>>k;
        cin>>s;
        cin>>x>>y;
        int cnt[n];
        memset(cnt,0,sizeof(cnt));
        int should[n];
        memset(should,0,sizeof(should));
        for (int i=n-1;i>=n-k;i--){
            int xx=0;
            int fk = 1;
            for (int j=i;j>=0;j-=k){
                xx+=s[j]-'0';
                cnt[j]+=xx;
                should[j]+=fk;
                fk++;
            }
        }
        p--;
        int ans = 1000000000;
        for (int i=0;i<n;i++){
            if (i+p>=n) break;
            int left = n-i-p;
            int m = should[i+p]-cnt[i+p];
            int cur = i*y+m*x;
            ans=min(ans,cur);
        }
        cout<<ans<<endl;
    }
}