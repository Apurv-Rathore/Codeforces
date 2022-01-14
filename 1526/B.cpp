#include <bits/stdc++.h>
using namespace std;
#define fastio                    \
    ios_base::sync_with_stdio(0); \
    cin.tie(0);                   \
    cout.tie(0);
#define rep(i, s, e) for (int i = s; i < e; i++)
#define rrep(i, s, e) for (int i = s; i > e; i--)
#define srep(i, s, e, j) for (int i = s; i < e; i += j)
#define tr(i, x) for (auto i : x)
#define int long long
#define vi vector<int>
#define vs vector<string>
#define vb vector<bool>
#define vpi vector<pii>
#define maxpqi priority_queue<int>
#define minpqi priority_queue<int, vector<int>, greater<int>>
#define pii pair<int, int>
#define F first
#define S second
#define mk make_pair
#define pb push_back
#define pf push_front
#define endl '\n'
#define br printf("\n")
#define inf 10000000000
#define negainf LLONG_MIN
#define imap map<int, int>
#define uimap unordered_map<int, int>
#define gcd(a, b) __gcd(a, b)
#define sumv(a) accumulate(a.begin(), a.end(), 0)
#define suma(a, n) accumulate(a, a + n, 0)
#define maxv(a) max_element(a.begin(), a.end()) // gives pointer to max value
#define maxa(a, n) max_element(a, a + n)        // gives pointer to max value
#define max3(a, b, c) max(max((a), (b)), (c))
#define max4(a, b, c, d) max(max((a), (b)), max((c), (d)))
#define min3(a, b, c) min(min((a), (b)), (c))
#define min4(a, b, c, d) min(min((a), (b)), min((c), (d)))
#define mod 1000000007
#define clr(x) memset(x, 0, sizeof(x))
#define fill(x, y) memset(x, y, sizeof(x))
#define lb lower_bound
#define ub upper_bound
#define npos string::npos
#define all(x) x.begin(), x.end()
#define descen greater<int>()
#define si1(a) scanf("%d", &a)
#define si2(a, b) scanf("%d %d", &a, &b)
#define ss1(a) scanf("%d", &a)
#define pi1(a) printf("%d ", a)
#define pi2(a, b) printf("%d %d ", a, b)
#define pl1(a) printf("%lld ", a)
#define pt printf
int mod1 = 1000000007;

string yes = "YES", no = "NO";




void solve()
{
    int n;
    cin >> n;
    int fg = 0;
    int cnt=0;
    for(int i=0;i<20;i++){
        if (i*111>n ) {
            cnt+=1;
            if (cnt==0) cnt=1;
            break;
        }
        if ((n-i*111)%11==0){
            cnt+=1;
            if (cnt==0) cnt=1;
            fg =  1;
            break;
        }
    }
    if (fg==1) cout<<"YES"<<endl;
    else cout<<"NO"<<endl;
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
    cin >> t;
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