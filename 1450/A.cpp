#include <bits/stdc++.h>
#include<vector>
//#define ll long long int  
#define endl "\n"
using namespace std;

int main()
{
    
    int t;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        string s;
        cin>>s;
        string ans = "";
        for (auto i:s)
        {
            if (i=='b')
            {
                ans = 'b' + ans;
            }
            else
            {
                ans+=i;
            }
        }
        cout<<ans<<endl;
    
        
    }
}