class Solution {
    public int firstMissingPositive(int[] nums) {
        //decide whether there is 1
        //set < 0 and > n as the number
        int N = nums.length;
        int contains = 0;
        for(int i = 0; i < N; i++){
            if(nums[i] == 1)
            {
                contains++;
            }else if(nums[i] <= 0 || nums[i] > N){
                nums[i] = 1;
            }
        }
        if(contains == 0)return 1;
        for(int i = 0; i < N; i++){
            int idx = Math.abs(nums[i]) - 1;
            
            nums[idx] = -Math.abs(nums[idx]);
        }
        
        for(int j = 0; j < N; j++){
            if(nums[j] > 0)return j + 1;
        }
        return N + 1;
        

    }
}