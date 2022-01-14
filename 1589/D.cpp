#include<bits/stdc++.h>
#define int long long
using namespace std;int query(int l,int r){
    cout<<"? "<<++l<<" "<<++r<<endl;int x;cin>>x;return x;    
}
signed main(){
    int t;int n;cin>>t;
    while (t--){
        cin>>n;
        int total = query(0,n-1);
        int k = n+1;
        int low = 0, high = n-1;
        while (low<=high){
            int mid = (low+high)/2;
            int res = query(0,mid);
            if (res==total){
                k = min(k , mid);high = mid-1;
            }
            else low = mid+1;            
        }
        int j = query(0,k) - query(0,k-1);j = k - j;
        int i = query(0,j-1) - query(0,j-2);i = j-1-i;
        cout<<"! "<<i+1<<" "<<j+1<<" "<<k+1<<endl;
    }
    return 0;
}