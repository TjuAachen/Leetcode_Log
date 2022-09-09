class Solution {
    public int maxSubArray(int[] nums) {
        int res = 0;
        int ans = nums[0];
        for(int i = 0; i < nums.length; i++){
            res = Math.max(res + nums[i], nums[i]);
            ans = Math.max(res, ans);
        }
        return ans;
        
    }
}