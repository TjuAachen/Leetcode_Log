class Solution {
    public int maxSubarraySumCircular(int[] nums) {
        int n = nums.length;
        int[] rightMax = new int[n];
        int suffixSum = nums[n - 1];
        rightMax[n - 1] = nums[n - 1];
        
        for (int i = n - 2; i >= 0; i--) {
            suffixSum += nums[i];
            rightMax[i] = Math.max(rightMax[i + 1], suffixSum);
        }
        
        int curMax = Integer.MIN_VALUE;
        int normalMax = Integer.MIN_VALUE;
        int prefixSum = 0;
        int specialSum = Integer.MIN_VALUE;
        
        int[] leftMax = new int[n];
        
        for (int j = 0; j < n; j++) {
            normalMax = Math.max(0, normalMax) + nums[j];
            curMax = Math.max(curMax, normalMax);
            prefixSum += nums[j];
            
            if (j + 1 < n) {
                specialSum = Math.max(specialSum, prefixSum + rightMax[j + 1]);
            }
        }
        
        return Math.max(specialSum, curMax);
    }
}