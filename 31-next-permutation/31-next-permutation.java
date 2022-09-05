class Solution {
    public void nextPermutation(int[] nums) {
        int[] rightMax = new int[nums.length];
        LinkedList<Integer> stack = new LinkedList<>();
        for(int i = 0; i < nums.length; i++)
            for(int j = i + 1; j < nums.length; j++){
                if(nums[j] > nums[i]) rightMax[i] = Math.max(rightMax[i], j);        
            }
        int rightMost = -1;
        for(int j = nums.length - 1; j > - 1; j--){
            if(rightMax[j] != 0){
                rightMost = Math.max(rightMost, j);
            }
        }
        if (rightMost != -1){
            int temp = nums[rightMost];
            nums[rightMost] = nums[rightMax[rightMost]];
            nums[rightMax[rightMost]] = temp;
            Arrays.sort(nums, rightMost+1, nums.length);
        }else{
            reverse(nums);
        }
    }
    public void reverse(int[] nums){
        for(int i = 0; i < nums.length / 2; i++){
            int temp = nums[i];
            nums[i] = nums[nums.length - i - 1];
            nums[nums.length - i - 1] = temp;
        }
    }
}