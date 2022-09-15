class Solution {
    public void sortColors(int[] nums) {
        int N = nums.length;
        int less = 0, larger = N - 1;
        for(int i = 0; i <= larger ;){
            if(nums[i] == 0){
                int temp = nums[i];
                nums[i] = nums[less];
                nums[less] = temp;
                less++;
                i++;
            }else if(nums[i] == 2){
                int temp = nums[i];
                nums[i] = nums[larger];
                nums[larger] = temp;
                larger--;
            }else{i++;}
        }

        
    }
}