//amazing takes time, legendary requires patience
#include "bits/stdc++.h"
#define sd(n) scanf("%d", &(n))
#define rep(i, x, n) for (int i = x, _n = (n); i < _n; ++i)
#define repi(i, a) for(typeof((a).begin()) i = (a).begin(), _##i = (a).end(); i != _##i; ++i)
#define pra(v) repi(it, v) cout << *it << " "; cout << endl;
#define SZ(c) (int)(c).size()
#define lcm(a,b) (a*(b/__gcd(a,b)))
#define VI vector<int>
#define all(c) (c).begin(), (c).end()
#define allr(c) (c).rbegin(), (c).rend()
#define pb push_back
#define mii map<int, int>
#define pii pair<int, int>
#define pip pair<int, pii>
#define F first
#define S second
#define mp make_pair
#define lli long long int
#define llu unsigned long long
#define CLR(p) memset(p, 0, sizeof(p))
#define SET(p) memset(p, -1, sizeof(p))
#define INF 0x3f3f3f3f
#define pi 3.141592653589793
#define debug 0
using namespace std;

const int MOD = 1e9+7;
const int MAX = 1000010;
const double eps = -1e8;

int n, m, a[MAX];
int can[1024][1024];

int main()
{
	ios_base::sync_with_stdio(0);
	cin >> n >> m;
	rep(i, 0, n)
	{
		cin >> a[i];
		a[i] %= m;
	}
	if(n > m)	//pigeonhole principle
	{
		//answer is always yes
		cout << "YES\n";
		return 0;
	}
	else
	{
		rep(i, 0, n+1)		
			can[i][0] = 1;
		rep(i, 1, n+1)
		{
			rep(r, 0, m+1)
			{
				can[i][r] = (can[i-1][(r - a[i-1] + m)%m] || can[i-1][r]);
			}
		}
		if(can[n][m])
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	
    return 0;
}    