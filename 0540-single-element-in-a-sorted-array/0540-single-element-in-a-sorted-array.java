class Solution {
    public int singleNonDuplicate(int[] nums) {
        int left = 0;
        int right = nums[nums.length - 1];
        
        while (left + 1 < right) {
            int mid = left + (right - left) / 2;
            int count = bisect_right(mid, nums) + 1;
            //  System.out.printf("%d %d\n", mid, count);
            if (count % 2 == 0) {
                left = mid;
            }else {
                right = mid;
            }
        }
        int countLeft = bisect_right(left, nums) + 1;
        //System.out.printf("%d %d\n", left, countLeft);
        if (countLeft % 2 == 1)
            return left;
        return right;
        
        
        
    }
    
    // find largest index with val <= target
    public int bisect_right(int target, int[] nums) {
        int left = 0;
        int right = nums.length - 1;
        
        while (left + 1 < right) {
            int mid = (left + right) / 2;
            
            if (nums[mid] <= target) {
                left = mid;
            }else {
                right = mid;
            }
        }
        if (nums[right] <= target)
            return right;
        if (nums[left] <= target)
            return left;
        return -1;
        
    }
    
}