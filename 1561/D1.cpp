#include <bits/stdc++.h>
#define int long long
using pii=std::pair<int,int>;
using namespace std;
 
const int maxn = 4e6 + 5;
 
int n, m, ans[maxn], diff[maxn], prefans[maxn];
int32_t main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cin >> n >> m;
    prefans[0] = 0;
    diff[1] = 1;
    diff[2] = -1;
    for(int i = 1; i <= n; i++)
    {
        diff[i] += diff[i - 1];
        diff[i] %= m;
        ans[i] = (diff[i] + prefans[i - 1]);
        ans[i] %= m;
        prefans[i] = prefans[i - 1] + ans[i];
        prefans[i] %= m;
        for(int mult = 2; i * mult <= n; mult++)
        {
            int from = i * mult;
            int to = (i + 1) * mult;
            diff[from] += ans[i];
            diff[from] %= m;
            diff[to] += (m - ans[i]);
            diff[to] %= m;
        }
    }
    cout << ans[n] << "\n";
    return 0;
}