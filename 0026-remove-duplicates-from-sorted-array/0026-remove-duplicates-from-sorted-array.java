class Solution {
    public int removeDuplicates(int[] nums) {
        int N = nums.length;
        int k = 1;
        int prev = -101;
        for(int i = 1; i < N; i++){
            if (nums[i] != nums[i-1] && nums[i] > nums[k-1]){
                prev = nums[k];
                int temp = nums[i];
                nums[i] = nums[k];
                
                nums[k] = temp;
                
                k++;
            }
            
        }
        return k;
    }
}