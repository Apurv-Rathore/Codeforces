#include<bits/stdc++.h>
#define ll long long
#define fastio ios_base::sync_with_stdio(false),cin.tie(NULL),cout.tie(NULL);
using namespace std;

int main(){
    fastio
    int t; cin>>t;
    while(t--){
        int n; cin>>n;
        int a[n];
        for(int i=0; i<n; i++){
            cin>>a[i];
            a[i]--;
        }
        vector<vector<int>>cnt;
        vector<vector<int>>ind;
        for (int i=0; i<200; i++){
            vector<int>cnt1(n,0);
            vector<int>ind1;
            cnt.push_back(cnt1);
            ind.push_back(ind1);
        }
        for (int i=0; i<n; i++){
            cnt[a[i]][i]++;
            ind[a[i]].push_back(i);
        }
        for(int i=0; i<200; i++){
            for(int j=1; j<n; j++){
                cnt[i][j] += cnt[i][j-1];
            }
        }

        int ans = 0;
        for (int i=0; i<200; i++){
            int l=0, r = ind[i].size()-1;
            int tans = 0, ttans = 0;
            while(l<r){
                ttans += 2;
                for(int j=0; j<200; j++){
                    ttans += cnt[j][ind[i][r]-1]-cnt[j][ind[i][l]];
                    tans = max(tans,ttans);
                    ttans -= cnt[j][ind[i][r]-1]-cnt[j][ind[i][l]];
                }
                l++;
                r--;
                ans = max(ans,tans);
            }
        }
        for(int i=0; i<200; i++){
            ans = max(ans, cnt[i][cnt[i].size()-1]);
        }
        cout<<ans<<'\n';
    }
    return 0;
}