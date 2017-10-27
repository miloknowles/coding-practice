/* Return the maximum product of a contiguous subarray in an array */

int maxProduct(vector<int>& nums) {
    int best = nums[0];
    
    int dp[nums.size()][2];
    
    dp[0][0] = nums[0];
    dp[0][1] = nums[0];
    
    for (int i = 1; i < nums.size(); i++) {
        dp[i][0] = min(min(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i]), nums[i]);
        dp[i][1] = max(max(dp[i-1][0] * nums[i], dp[i-1][1] * nums[i]), nums[i]);
        if (dp[i][1] > best) { best = dp[i][1]; }
    }
    return best;
}