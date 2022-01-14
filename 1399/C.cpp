/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int i;
        int j;
        int q,n,s,x,k,f;
        cin>>n;
        vector <int> l;
        for (int i=0;i<n;i++)
        {
            cin>>f;
            l.push_back(f);
        }
        int m = 0;
        for (int i=2;i<2*n+1;i++)
        {
            int v[n];
            for (int i=0;i<n;i++)
            {
                v[i]=0;
            }
            int cc=0;
            for (int j=0;j<n-1;j++)
            {
                for (int k=j+1;k<n;k++)    
                {
                    if (l[j]+l[k]==i and v[j]==false and v[k]==false)
                    {
                        cc = cc+1;
                        v[k]+=1;
                        v[j]+=1;
                        
                    }
                }
                if (m<cc)
                {
                    m=cc;
                }
            }
        }
        cout<<m<<endl;
    }

    return 0;
}
