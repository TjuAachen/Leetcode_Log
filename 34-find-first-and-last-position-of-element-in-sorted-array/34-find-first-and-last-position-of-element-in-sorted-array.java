class Solution {
    public int[] searchRange(int[] nums, int target) {
        //find the leftmost
        int leftMost = findOccurrence(nums, 0, nums.length - 1, target, true);
        int rightMost = findOccurrence(nums, 0, nums.length - 1, target, false);
        return new int[]{leftMost, rightMost}; 
    }
    public int findOccurrence(int[] nums, int left, int right, int target, boolean isFirst){
           while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target){
                if(!isFirst){
                    if(mid == nums.length - 1 || (nums[mid+1] != target))return mid;
                    left = mid + 1;
                    
                    
                }else{
                    if(mid == 0 || (nums[mid-1] != target))return mid;
                    right = mid - 1;
                                        
                }

            }else if(nums[mid] > target){
                right = mid - 1;
            }else{
                left = mid + 1;
            }
        }     
        return -1;
        
        
        
        
    }
}