#include <bits/stdc++.h>
using namespace std;
#define fastio ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
#define rep(i,s,e) for(int i=s ; i < e ; i++)
#define rrep(i,s,e) for(int i=s ; i > e ; i--)
#define srep(i,s,e,j) for(int i=s ; i < e ; i+=j)
#define tr(i,x) for(auto i : x)
#define int long long
#define vi vector<int>
#define vs vector<string>
#define vb vector<bool>
#define vpi vector<pii>
#define maxpqi priority_queue<int>
#define minpqi priority_queue <int, vector<int>, greater<int> >
#define pii pair<int,int> 
#define F first
#define S second
#define mk make_pair
#define pb push_back
#define pf push_front
#define endl '\n'
#define br printf("\n")
#define inf 10000000000
#define negainf LLONG_MIN
#define imap map<int,int>   
#define uimap unordered_map<int,int>
#define gcd(a,b) __gcd(a,b)
#define sumv(a) accumulate(a.begin(),a.end(),0)
#define suma(a,n) accumulate(a,a+n,0)
#define maxv(a) max_element(a.begin(),a.end()) // gives pointer to max value 
#define maxa(a,n) max_element(a,a+n) // gives pointer to max value
#define max3(a,b,c) max(max((a),(b)),(c))
#define max4(a,b,c,d) max(max((a),(b)),max((c),(d)))
#define min3(a,b,c) min(min((a),(b)),(c))
#define min4(a,b,c,d) min(min((a),(b)),min((c),(d)))
#define mod 1000000007
#define clr(x) memset(x,0,sizeof(x))
#define fill(x,y) memset(x,y,sizeof(x))
#define lb lower_bound
#define ub upper_bound
#define npos string::npos
#define all(x) x.begin(),x.end()
#define descen greater<int>()
#define si1(a) scanf("%d",&a)
#define si2(a,b) scanf("%d %d",&a,&b)
#define ss1(a) scanf("%d",&a)
#define pi1(a) printf("%d ",a)
#define pi2(a,b) printf("%d %d ",a,b)
#define pl1(a) printf("%lld ",a)
#define pt printf
int mod1 = 1000000007;

string yes="YES",no="NO";

vector<vector<vector<int> > >sumtok;


int n,m;
int dp[501][501][15];
vector<vector<int> > horizontal;
vector<vector<int> > vertical;
int fun(int i,int  j,int k,int n,int m){
    if (k==0) return 0;
    if (i<0 or j<0 or i>=n or j>=m){
        return inf;
    }
    int ans = inf;
    if (dp[i][j][k]!=-1){
        return dp[i][j][k];
    }
    int ans1 = inf; //left
    if (j>0){
        ans1 = horizontal[i][j-1]+fun(i,j-1,k-1,n,m);
    }
    int ans2 = inf; //up
    if (i>0){
        ans2 = vertical[i-1][j]+fun(i-1,j,k-1,n,m);
    }
    int ans3 = horizontal[i][j]+fun(i,j+1,k-1,n,m);
    int ans4 = vertical[i][j]+fun(i+1,j,k-1,n,m);
    dp[i][j][k]=min4(ans1,ans2,ans3,ans4);
    // cout<<ans1<<" "<<ans2<<" "<<ans3<<" "<<ans4<<endl;
    return min4(ans1,ans2,ans3,ans4);



    // cout<<"5 SIZE" << sumtok[5].size()<<endl;
    // return 0;

    // for (int aa=0;aa<sumtok[k].size();aa++){
    //     int x1 = sumtok[k][aa][0];
    //     int x2 = sumtok[k][aa][1];
    //     int x3 = sumtok[k][aa][2];
    //     int x4 = sumtok[k][aa][3];
    //     int temp=0;
    //     if (x1>0)
    //         temp+=vertical[i][j]+fun(i+1,j,x1-1,n,m);
    //     if (x2>0)
    //         temp+=horizontal[i][j]+fun(i,j+1,x2-1,n,m);
    //     if (x3>0)
    //         if (i==0)
    //             temp+=1000000000;
    //         else
    //             temp+=vertical[i-1][j]+fun(i-1,j,x3-1,n,m);
    //     if (x4>0)
    //         if (j==0)
    //             temp+=1000000000;
    //         else
    //             temp+=horizontal[i][j-1]+fun(i,j-1,x4-1,n,m);
    //     ans=min(ans,temp);
    // }
    dp[i][j][k]=ans;
    // cout<<ans<<endl;
    // return 0;
    return ans;
        
}


void solve(){
    memset(dp,-1,sizeof(dp));
    int k;
    cin>>n>>m>>k;
    
    vector<int> temp;
    rep(i,0,n){
        for (int j=0;j<m-1;j++){
            int x;
            cin>>x;
            temp.push_back(x);
        }
        temp.push_back(inf);
        horizontal.push_back(temp);
        temp.clear();
    }
    rep(i,0,n-1){
        temp.clear();
        for (int j=0;j<m;j++){
            int x;
            cin>>x;
            temp.push_back(x);
        }
        temp.push_back(inf);
        vertical.push_back(temp);
        temp.clear();
    }
    rep(i,0,m) temp.push_back(inf);
    vertical.push_back(temp);
    if (k%2==1){
        rep(i,0,n){
            for (int j=0;j<m;j++){
                cout<<-1<<" ";
            }
            cout<<endl;
        }
        return;
    }
    // return ;

    rep(i,0,n){
        for (int j=0;j<m;j++){
            int ans = fun(i,j,k/2,n,m)*2;
            cout<<ans<<" ";
        }
        cout<<endl;
    }

}

int32_t main()
{
    fastio
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE 
		freopen("input.txt", "r", stdin); 
		freopen("output.txt", "w", stdout); 
	#endif
    int t;
    t = 1;
    // cin>>t;
    while (t--)
    {
        solve();
    }
    
    return 0;
}


// for finding number of distinct prime factors, 
// for i in range(2,a):
// for j in range(i,a,j):
// primeFactors[j]+=1
// ______________________________________________________________
// for finding sum of powers of prime factors
// for(int i=2;i<=N;++i)if(!c[i])for(int j=i;j<=N;j+=i)c[j]=i;
// for(int i=2;i<=N;++i)c[i]=1+c[i/c[i]],d[i]=c[i]+d[i-1];
/*
// Sort the array in descending order 
    sort(arr, arr + n, greater<int>()); 
*/