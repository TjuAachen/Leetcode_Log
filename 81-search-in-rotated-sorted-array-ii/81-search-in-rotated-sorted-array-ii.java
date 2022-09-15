class Solution {
    int N;
    public boolean search(int[] nums, int target) {
        N = nums.length - 1;
        int leftMark = findLeftMark(nums);
        if(nums[0] == target)return true;
        if(leftMark == N + 1)return false;
        //leftMark is the first number not equal to nums[0]
        int left = 0, right = N;
        
        
        while(left <= right){
            int mid = left + (right - left) / 2;
            int curNum = nums[mid];
            if(curNum == target)return true;
            if(curNum < target){
                if(curNum > nums[0]){
                    left = mid + 1;
                }else if(curNum < nums[0]){
                    if(target > nums[0]){
                        right = mid -1;
                    }else{
                        left = mid + 1;
                    }
                }else{
                    if(mid < leftMark){
                        left = mid+1;
                    }else{
                        right = mid - 1;
                    }
                }
            }else{
                if(curNum < nums[0]){
                    right = mid - 1;
                }else if(curNum > nums[0]){
                    if(target > nums[0]){
                        right = mid - 1;
                    }else{
                        left = mid + 1;
                    }
                    
                }else{
                    if(mid < leftMark){
                        left = mid + 1;
                    }else{
                        right = mid - 1;
                    }
                    
                }
            }
        }
        return false;
        
    }
    
    public int findLeftMark(int[] nums){
        int i = 0;
        while(i <= N && nums[0] == nums[i]){
            i++;
        }
        return i;
    }
    
}
