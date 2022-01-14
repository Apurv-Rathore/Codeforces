#include <bits/stdc++.h>
#define fastio ios_base::sync_with_stdio(false), cin.tie(NULL);
#define ll long long
using namespace std;

const int maxn = 1e5 + 5;
vector<int>graph[maxn];

int main(){
    fastio
    int n; cin>>n;
    for(int i=0; i<n-1; i++){
        int ai,bi; cin>>ai>>bi;
        ai--;bi--;
        graph[ai].push_back(bi);
        graph[bi].push_back(ai);
    }
    int leaves = 0;
    int neigh = 0;
    int root = -1;
    unordered_set<int>s;
    for(int i=0; i<n; i++){
        if (graph[i].size()==1){
            if (root == -1) root = i;
            s.insert(i);
            leaves++;
        }
    }
    for (int i=0; i<n; i++){
        for(auto j: graph[i]){
            if (s.find(j) != s.end()){
                neigh++;
                break;
            }
        }
    }
    

    int vis[n];
    fill(vis, vis+n, 0);
    vector<int>stack;
    stack.push_back(root);
    vis[root]=1;
    int dist[n];
    dist[root]=0;
    while(!stack.empty()){
        int curr = stack.back();
        stack.pop_back();
        for(int i=0; i<graph[curr].size(); i++){
            if (!vis[graph[curr][i]]){
                vis[graph[curr][i]]=1;
                dist[graph[curr][i]]=dist[curr]+1;
                stack.push_back(graph[curr][i]);
            }
        }
    }

    int mini = 1;
    for(int i=0; i<n; i++){
        if (graph[i].size()==1 && dist[i]%2 && mini==1) mini=3;
    }

    // cout<<"h "<<leaves<<' '<<neigh<<endl;

    cout<<mini<<' '<<n-1-leaves+neigh<<endl;
    return 0;
}