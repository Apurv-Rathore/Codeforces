#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define ll long long
using namespace std;


int main(){
    #ifndef ONLINE_JUDGE
        freopen("input.txt", "r", stdin);
        freopen("output.txt", "w", stdout);
    #endif
    fastio
    int t;
    cin>>t;
    while(t--){
            int n,m,k;
            cin>>n>>m>>k;
            if (n==1){
                if (k>=m/2){
                    cout<<"Yes"<<endl;
                }
                else{
                    cout<<"No"<<endl;
                }
                continue; ;
            }           
            if (m==1){
                if (k==0) cout<<"Yes"<<endl;
                else cout<<"No"<<endl;
                continue;
            } 
            if (n%2==1){
                int x;
                x = m/2;
                if (k<x) {
                    cout<<"No"<<endl;
                    continue;
                }
                if ((k-x)%2==1){
                    cout<<"No"<<endl;
                }
                else{
                    cout<<"Yes"<<endl;
                }
                continue;
            }
            if (n%2==0 and m%2==1){
                int x = k;
                x=(n*m)/2-x;
                if (x<n/2){
                    cout<<"No"<<endl;
                    continue;
                }
                x-=n/2 ;
                if (x%2==0){
                    cout<<"Yes"<<endl;
                    continue;
                }
                cout<<"No"<<endl;
                continue;
            }
            if (n%2==0 and m%2==0){
                if(k%2==0) cout<<"Yes"<<endl;
                else cout<<"No"<<endl;
            }


        }
    
}