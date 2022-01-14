#include<bits/stdc++.h>
#define int long long
using namespace std;
signed main(){
    int t;
    cin>>t;
    while (t--){
        int n,m;
        cin>>n>>m;
        int res = (n*m)/3;
        if ((n*m)%3!=0) res++;
        cout<<res<<endl;
    }
    return 0;
}