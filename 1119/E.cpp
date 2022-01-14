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
#define inf 1000000
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
    vi l(n, 0);
    rep(i, 0, n) cin >> l[i];
    if (n == 1)
    {
        cout << l[0] / 3 << endl;
        return;
    }
    int rest = 0;
    int ans = 0;
    rep(i, 0, n)
    {
        rest+=l[i];
        if (i == 0)
        {
            if (l[i] >= 3)
            {
                int m = l[i] / 3;
                l[i] -= 3 * m;
                ans += m;       
                rest-=3*m;
            }
            continue;
        }
        if (l[i] > 1)
        {
            int m = min(rest-l[i], l[i] / 2);
            l[i] -= 2 * m;
            ans += m;
            rest -= 3 * m;
        }
        if (l[i] >= 3)
        {
            int m = l[i] / 3;
            l[i] -= 3 * m;
            rest -= 3 * m;
            ans += m;
        }
    }
    cout << ans << endl;
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

/*
// Sort the array in descending order 
    sort(arr, arr + n, greater<int>()); 
*/