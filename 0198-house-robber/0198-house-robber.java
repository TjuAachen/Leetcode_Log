class Solution {
    public int rob(int[] nums) {
        int res = nums[0];
        int n = nums.length;
        int[] maxAmount = new int[n];
        
        maxAmount[0] = nums[0];
        
        for (int i = 1; i < n; i++){   
            maxAmount[i] = nums[i];
            int temp = 0;
            for (int j = 0; j < i - 1; j++)
                temp = Math.max(temp, maxAmount[j]);

            res = Math.max(res, maxAmount[i] + temp);
            maxAmount[i] = res;
        }
        
        return res;
    }
}