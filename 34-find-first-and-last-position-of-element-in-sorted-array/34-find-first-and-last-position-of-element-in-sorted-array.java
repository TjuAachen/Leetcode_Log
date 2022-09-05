class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        //find the leftmost
        int leftMost = -1, rightMost = -1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target){
                if(mid == 0 || (nums[mid-1] != target)){
                    leftMost = mid;
                    break;
                }else{
                    right = mid - 1;
                }
            }else if(nums[mid] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        
        left = 0; right = nums.length - 1;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target){
                if(mid == nums.length - 1 || (nums[mid+1] != target)){
                    rightMost = mid;
                    break;
                }else{
                    left = mid + 1;
                }
            }else if(nums[mid] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }
        return new int[]{leftMost, rightMost};
        
        
        
    }
}