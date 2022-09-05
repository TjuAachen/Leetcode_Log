class Solution {
    public int search(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
         
        while(left <= right){
            int mid = left + (right - left) / 2;
            int curVal = nums[mid];
            if(curVal == target){
                return mid;
            }else if(curVal < target){
                //decide it's left or right
                if(curVal >= nums[0]){
                    left = mid + 1;
                }else{
                 //right
                    if(target < nums[0]){
                        left = mid + 1;
                    }else{
                        right = mid - 1;
                    }
                    
                }
            }else{
                //decide it's left or right
                if(curVal >= nums[0]){
                    if(target >= nums[0]){
                        right = mid - 1;
                    }else{
                        left = mid + 1;
                    }
                }else{
                 //right
                    right = mid - 1;
                    
                }                
            }   
        }
        return -1;
        
    }
}