class Solution {
    public long countSubarrays(int[] nums, int minK, int maxK) {

        long res = 0;
        int leftPossible = Integer.MAX_VALUE;
        int rightMostMin = -1;
        int curMaxIdx = -1;
        int curMax = Integer.MIN_VALUE;
        int i = 0;
        
        for (int num : nums) {
            if (num < minK || num > maxK) {
                leftPossible = Integer.MAX_VALUE;
                rightMostMin = -1;
                curMax = Integer.MIN_VALUE;
            }

            if (num >= minK && num <= maxK) {
                leftPossible = Math.min(leftPossible, i);
                curMax = Math.max(curMax, num);
            }
            
            if (num == minK) {
                rightMostMin = i;
            }
            if (num == maxK) {
                curMaxIdx = i;
            }
            
            if (curMax == maxK && rightMostMin != -1 && leftPossible != Integer.MAX_VALUE) {
                
                res += (long) (Math.min(rightMostMin, curMaxIdx) - leftPossible + 1);
            }
            
            i++;
        }
        
        return res;
    }
}