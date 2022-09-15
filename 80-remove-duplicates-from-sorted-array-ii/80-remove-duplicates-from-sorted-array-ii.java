class Solution {
    public int removeDuplicates(int[] nums) {
        int k = 0;
        for(int i = 0; i < nums.length; i++){
            if(k >= 2 && nums[i] > nums[k-2]){
                int temp = nums[k];
                nums[k] = nums[i];
                nums[i] = temp;
                k++;
            }else if (k < 2){
                k++;
            }
        }
        return k;
    }
}