class Solution {
    public int firstMissingPositive(int[] nums) {
        //1 是否在其中
        //if no 1, 1 is the missing
        int min = Integer.MAX_VALUE;
        for(int k = 0; k < nums.length; k++){
            if (nums[k] < 0)continue;
            if(nums[k] == 0){
                nums[k] = -1;
                continue;
            }
            min = Math.min(nums[k], min);      
        }
        if(min != 1)return 1;
        //不能超过nums的长度
        int upperLimit = nums.length + 1;
        for(int i = 0; i < nums.length;){
            int curVal = nums[i];
            if(curVal >= upperLimit||curVal <= 0)
            {
                i++;
                continue;
            }
             
            int idx = curVal - 1;
            int targetVal = nums[idx];
            if(targetVal >= upperLimit || targetVal <= 0)
            {
                nums[idx] = 0;
                i++;
            
            }else if(idx == i){
                nums[i] = 0;
                i++;
            }else{
                nums[i] = targetVal;
                nums[idx] = 0;
            }
        }
        int j = 0;
        while(j < nums.length){
            if(nums[j] != 0) return j+1;
            j++;
        }
        return nums.length + 1;            
        }    
}