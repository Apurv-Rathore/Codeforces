#include<bits/stdc++.h>
#define N 1000005
#define int long long
using namespace std;
int T,n,k,a[N],xo,u,v,cnt;
vector<int>ve[N];

int dfs(int now,int fa){
	int sum=a[now];
	for(int i=0;i<ve[now].size();i++){
		int y=ve[now][i];
		if(y==fa)continue;
		sum^=dfs(y,now);
	}	
	if(sum==xo)cnt++,sum=0;
	return sum;
}
signed main(){
	cin>>T;
	while(T--){
		cin>>n>>k;
		for(int i=1;i<=n;i++)cin>>a[i],xo^=a[i];
		for(int i=1;i<n;i++){
			cin>>u>>v;
			ve[u].push_back(v);
			ve[v].push_back(u);
		}
		if(xo==0)puts("YES");
		else{
			dfs(1,0);
			if(cnt>=2&&k>=3)puts("YES");
			else puts("NO");
		}
		xo=0;
		for(int i=1;i<=n;i++)ve[i].clear();
		cnt=0;
	}
}