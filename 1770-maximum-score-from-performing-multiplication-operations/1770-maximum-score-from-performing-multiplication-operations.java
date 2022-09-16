class Solution {
    Map<Pair, Integer> memo = new HashMap<>();
    int n;
    int m;
    public int maximumScore(int[] nums, int[] multipliers) {
        n = nums.length; m = multipliers.length;
        int[][] dp = new int[m+1][m+1];
        int ans = Integer.MIN_VALUE;
        for(int head = 0; head < m + 1; head++)
            for(int tail = 0; tail < m + 1 - head; tail++){
                int left = Integer.MIN_VALUE;
                int right = Integer.MIN_VALUE;
                int p = head + tail - 1;
                if(p < m && p>= 0){
                    if(tail > 0){
                    right = Math.max(right,dp[head][tail-1] + nums[n - tail] * multipliers[p]);
                    }
                    if(head > 0){
                    left = Math.max(left,dp[head - 1][tail] + nums[head-1] * multipliers[p]);
                    }
                }else{
                    continue;
                }
                if(head == tail && head == 0){
                    dp[head][tail] = 0;
                }else{
                dp[head][tail] = Math.max(left, right);
                }
                if(head + tail == m){
                    ans = Math.max(ans, dp[head][tail]);
                }
    
            }
        return ans;


    }

}