#include <iostream>
#define int long long
using namespace std;


void solve()
{
    int n,k;
    cin>>n>>k;
    int l[n];
    for(int i=0;i<n;i++) cin>>l[i];
    int a = 10000000000000;
    for (int i=1;i<=100;i++)
    {
        int an = 0;
        for (int j=0;j<n;j++)
        {
            if(l[j]!=i)
            {
                an++;
                j+=k-1;
            }
        }
        a = min(a,an);
    }
    cout<<a<<endl;
    
}

signed main()
{
   int t;
   cin>>t;
   while(t--)
   {
   solve();    
   }
   
   
   return 0;
}