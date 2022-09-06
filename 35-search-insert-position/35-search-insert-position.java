class Solution {
    public int searchInsert(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        //find the floor
        int mid = 0;
        while(left <= right){
            mid = left + (right - left) / 2;
            if(nums[mid] == target) return mid;
            if(nums[mid] > target)right = mid - 1;
            if(nums[mid] < target){
                if(mid == nums.length - 1||nums[mid+1] > target){
                    break;
                }
                left = mid + 1;
            }
        }
        if(nums[mid] < target)return mid+1;
        return mid;
        

        
        
    }
}