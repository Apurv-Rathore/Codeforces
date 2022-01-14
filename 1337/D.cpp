// Template starts
#include <bits/stdc++.h>
#include <string>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#define fio                           \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL)
using namespace __gnu_pbds;
using namespace std;
#define gc getchar_unlocked
#define ll long long
#define inf INT_MAX
#define negainf INT_MIN
#define int long long int
#define fo(i, n) for (int i = 0; i < n; i++)
#define opp(i, n) for (int i = n - 1; i >= 0; i--)
#define one(i, n) for (int i = 1; i < n; i++)
#define lb lower_bound
#define ub upper_bound
#define si(x) scanf("%d", &x)
#define sl(x) scanf("%lld", &x)
#define ss(s) scanf("%s", s)
#define pi(x) printf("%d\n", x)
#define pl(x) printf("%lld\n", x)
#define ps(s) printf("%s\n", s)
#define deb(x) cout << #x << "=" << x << endl
#define deb2(x, y) cout << #x << "=" << x << "," << #y << "=" << y << endl
#define pb push_back
#define mp make_pair
#define F first
#define S second
#define all(x) x.begin(), x.end()
#define clr(x) memset(x, 0, sizeof(x))
#define sortall(x) sort(all(x))
#define tr(it, a) for (auto it = a.begin(); it != a.end(); it++)
#define PI 3.1415926535897932384626
#define max3(a, b, c) max(max((a), (b)), (c))
#define max4(a, b, c, d) max(max((a), (b)), max((c), (d)))
#define min3(a, b, c) min(min((a), (b)), (c))
#define min4(a, b, c, d) min(min((a), (b)), min((c), (d)))
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpii;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef unordered_map<int, int> unmap;
void solve();
string yes = "YES", no = "NO";
const int MOD = 1000000007;

int max(vi v)
{
    int res = 0;
    for (auto i : v)
    {
        if (res < i)
            res = i;
    }
    return res;
}

vpii primefac(ll n)
{
    vpii factors;
    int pow = 0;
    for (ll i = 2; i * i <= n; i++)
    {
        pow = 0;
        while (n % i == 0)
        {
            n = n / i;
            pow += 1;
        }
        if (pow > 0)
            factors.pb(mp(i, pow));
    }
    return factors;
}

ll mpow(ll a, ll b)
{
    a %= MOD;
    if (!b)
        return 1;
    ll temp = mpow(a, b / 2);
    temp = (temp * temp) % MOD;
    if (b % 2)
        return (a * temp) % MOD;
    return temp;
}

ll _pow(ll a, ll b)
{
    if (!b)
        return 1;
    ll temp = _pow(a, b / 2);
    temp = (temp * temp);

    if (b % 2)
        return (a * temp);
    return temp;
}

ll invmod(ll n)
{
    return mpow(n, MOD - 2);
}

int quotient(int a, int b)
{
    if (a % b == 0)
        return a / b;
    return 1 + a / b;
}

ll gcd(ll a, ll b)
{
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

pii findclosestsum(ll s)
{
    double a = 1, b = 1, c = -2 * s;
    double delta = 1 - 4 * a * c;
    double n = (-1 + sqrt(delta)) / 2;
    if (n == (ll)n)
        return {(ll)n, 1};
    return {(ll)n, 0};
}
vi psx;

void sieve(int n, map<int, int> &a1, map<int, int> &a2, map<int, int> &p)
{
    vi primes(n);
    primes[0] = 1;
    primes[1] = 1;
    fo(i, n)
    {
        if (primes[i])
            continue;
        for (int j = 2 * i; j < n; j += i)
        {
            primes[j] = 1;
        }
    }
    // can be easily extended to find smallest prime factor of any number k<=n
}

//Efficient Factorization
void factorize(ll a, map<int, int> &mpx)
{
    for (int d : {2, 3, 5})
    {
        if (a % d == 0)
            mpx[d]++;
        while (a % d == 0)
        {
            a = a / d;
        }
    }
    vi arr = {4, 2, 4, 2, 4, 6, 2, 6};
    int i = 0;
    for (ll d = 7; d * d <= a; d += arr[i++])
    {
        if (a % d == 0)
            mpx[d]++;
        while (a % d == 0)
        {
            a = a / d;
        }
        if (i == 8)
            i = 0;
    }
    if (a > 1)
        mpx[a]++;
}

const int maxn = 2e5 + 1;
int ncr(int n, int r)
{
    vector<unsigned long long> fac(16000, 1);
    if (n < r)
        return 0;
    return (fac[n] * invmod(fac[r]) % MOD * invmod(fac[n - r]) % MOD) % MOD;
}

template <typename T>
using oset = tree<T, null_type, less<T>, rb_tree_tag, tree_order_statistics_node_update>;
/*
    find_by_order() - Returns an iterator to the k-th largest element (counting from zero)
    order_of_key()  - The number of items in a set that are strictly smaller than our item
    Rest same as set
*/

// Template ends

int countbits(ll a)
{
    if (a == 0)
        return 0;
    int ans = 0;
    while (a > 0)
    {
        ans += 1;
        a = a / 2;
    }
    return ans;
}

int countdigits(ll a)
{
    if (a == 0)
        return 0;
    int ans = 0;
    while (a > 0)
    {
        ans += 1;
        a = a / 10;
    }
    return ans;
}
signed main()
{
    fio;

    int t;
    t = 1;
    cin >> t;
    while (t--)
    {
        solve();
    }
    return 0;
}

int res;
void fun(vi r, vi b, vi g)
{
    for (auto x:g)
    {   
        int y = lb(r.begin(),r.end(),x)-r.begin();
        int z = ub(b.begin(),b.end(),x)-b.begin()-1;
        auto yy = lb(r.begin(),r.end(),x);
        auto zz = ub(b.begin(),b.end(),x);
        if (y>=0 and z>=0 and y<r.size() and z<b.size())
        {

            y = r[y];
            z = b[z];
            res = min((x-y)*(x-y)+(y-z)*(y-z)+(x-z)*(x-z),res);
        }
    }
}
void solve()
{	
    
	int nr,nb,ng;
    cin>>nr>>nb>>ng;
    vector<int> r;
    vector<int> b;
    vector<int> g;
    int i,x;
    fo(i,nr)
    {
        cin>>x;
        r.pb(x);
    }
    fo(i,nb)
    {
        cin>>x;
        b.pb(x);
    }
    fo(i,ng)
    {
        cin>>x;
        g.pb(x);
    }
    sort(all(r));
    sort(all(b));
    sort(all(g));
    res = LLONG_MAX;
    fun(r,g,b);
    fun(r,b,g);
    fun(g,r,b);
    fun(g,b,r);
    fun(b,r,g);
    fun(b,g,r);
    cout<<res<<endl;



	
}	







