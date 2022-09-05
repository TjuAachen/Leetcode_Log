class Solution {
    public boolean search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        //find the real different one
        int leftMost = nums[0], rightMost = nums[nums.length - 1];
        int leftIdx = 0, rightIdx = nums.length - 1;
        while(leftIdx < nums.length && nums[leftIdx] == leftMost){
                leftIdx++;
            }
            if(leftIdx == nums.length){
                if (leftMost == target) return true;
                return false;
            }
        if(target == nums[0])return true;
        while(left <= right){
            int mid = left + (right - left) / 2;
            if(nums[mid] == target)return true;
            if(nums[mid] < target){                
                if(target > nums[0]){
                    if(nums[mid] > nums[0] ||(nums[mid] ==  nums[0]&& mid < leftIdx)){
                        left = mid + 1;
                    }else{
                        right = mid - 1;
                    }
                }else{
                    left = mid + 1;
                }
                    
                
            }else{
                if (target > nums[0]){
                    right = mid - 1;
                }else{
                    if(nums[mid] < nums[0] || (nums[mid] == nums[0] && mid > leftIdx)){
                        right = mid - 1;
                    }else{
                        left = mid + 1;
                    }
                }
            }
        }            
        return false;    
    }
    
}
