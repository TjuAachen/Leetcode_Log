class Solution {
    public int candy(int[] ratings) {
        int n = ratings.length;
        int[] nums = new int[n];
        
        //left
        nums[0] = 1;
        for(int i = 1; i < n; i++){
            if(ratings[i] > ratings[i-1]){
                nums[i] = nums[i-1] + 1;
            }else if(ratings[i] <= ratings[i-1]){
                nums[i] = 1;
            }
        }
        //right
        for(int i = n - 2; i >= 0; i--){
            if(ratings[i] > ratings[i+1]){
                nums[i] = Math.max(nums[i],nums[i+1] + 1);
            }
        }
        int ans = 0;
        for(int num : nums){
            ans += num;
        }
        return ans;
        
        
    }

    
    
}