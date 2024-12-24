class Solution {
public:
    int dist[100007];
    bool vis[100007];
    vector<vector<int>> e1, e2;
    vector<int> x;
    vector<int>q;

    int n, m;

    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        n = 0;
        m = 0;
        
        for(int i = 0; i < edges1.size(); i++)
            n = max(max(edges1[i][0], edges1[i][1]), n);
        for(int i = 0; i < edges2.size(); i++)
            m = max(max(edges2[i][0], edges2[i][1]), n);
        n++;
        m++;

        for(int i = 0; i < n; i++)
            e1.push_back(x);
        for(int i = 0; i < m; i++)
            e2.push_back(x);
        
        for(int i = 0; i < edges1.size(); i++)
        {
            e1[edges1[i][0]].push_back(edges1[i][1]);
            e1[edges1[i][1]].push_back(edges1[i][0]);
        }

        for(int i = 0; i < edges2.size(); i++)
        {
            e2[edges2[i][0]].push_back(edges2[i][1]);
            e2[edges2[i][1]].push_back(edges2[i][0]);
        }

        int diam1 = findDiameter1();
        int diam2 = findDiameter2();
        int diameter1 = diam1, diameter2 = diam2;
        if(diam1 % 2)
        {
            diam1 /= 2;
            diam1++;
        }
        else
        {
            diam1/=2;
        }

        if(diam2 % 2)
        {
            diam2 /= 2;
            diam2++;
        }
        else
        {
            diam2/=2;
        }
        return max(diam1 + diam2 + 1, max(diameter1, diameter2));
    }

    int findDiameter1()
    {
        int y = longestPath1(0);
        int z = longestPath1(y);
        return dist[z];
    }

    int longestPath1(int x)
    {
        for(int i = 0; i < n; i++)
        {
            vis[i] = false;
            dist[i] = 0;
        }
        dfs1(x);
        int ans = 0, node = x;
        for(int i = 0; i < n; i++)
        {
            if(dist[i] > ans)
            {
                ans = dist[i];
                node = i;
            }
        }
        return node;
    }

    void dfs1(int x)
    {
        vis[x] = true;
        for(int i = 0; i < e1[x].size(); i++)
        {
            int cur = e1[x][i];
            if(!vis[cur])
            {
                dist[cur] = dist[x] + 1;
                dfs1(cur);
            }
        }
    }

    int findDiameter2()
    {
        int y = longestPath2(0);
        int z = longestPath2(y);
        return dist[z];
    }

    int longestPath2(int x)
    {
        for(int i = 0; i < m; i++)
        {
            vis[i] = false;
            dist[i] = 0;
        }
        dfs2(x);
        int ans = 0, node = x;
        for(int i = 0; i < m; i++)
        {
            if(dist[i] > ans)
            {
                ans = dist[i];
                node = i;
            }
        }
        return node;
    }

    void dfs2(int x)
    {
        vis[x] = true;
        for(int i = 0; i < e2[x].size(); i++)
        {
            int cur = e2[x][i];
            if(!vis[cur])
            {
                dist[cur] = dist[x] + 1;
                dfs2(cur);
            }
        }
    }
};