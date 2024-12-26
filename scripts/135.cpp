class Solution {
public:

    int dp[20000 + 15];
    int candy(vector<int>& ratings) {
        int cnt = 1;
        int n = ratings.size();
        int ans = 0;
        dp[0] = 1;
        dp[n-1] = 1;
        for(int i=1; i<n; i++)
        {
            if(ratings[i] > ratings[i - 1])
            {    
                cnt++;
            }
            else
            {    
                cnt = 1;
            }
            dp[i] = cnt;
        }
        cnt = 1;
        ans = dp[n-1];
        for(int i=n-2; i>=0; i--)
        {
            if(ratings[i] > ratings[i + 1])
            {
                cnt++;
            }
            else
            {
                cnt = 1;
            }
            dp[i] = max(dp[i], cnt);
            ans += dp[i];
        }
        return ans;
    }
};