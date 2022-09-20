class Solution {
    public int findLength(int[] nums1, int[] nums2) {
        int n = nums1.length, m = nums2.length;
        int[][] dp = new int[n+1][m+1];
        int ans = 0;
        for(int i = 0; i < n + 1; i++)
            for(int j = 0; j < m + 1; j++){
                if(i == 0 || j == 0)continue;
                int curNum1 = nums1[i-1], curNum2 = nums2[j-1];
                if(curNum1 == curNum2){
                    dp[i][j] = dp[i-1][j-1] + 1;
                }
                ans = Math.max(ans, dp[i][j]);
            }
        return ans;
        
        
    }
}