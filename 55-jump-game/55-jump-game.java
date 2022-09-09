class Solution {
    public boolean canJump(int[] nums) {
        int Farthest = 0;
        for (int i = 0; i < nums.length; i++){
            if(i > Farthest)return false;
            Farthest = Math.max(Farthest, nums[i] + i); 
        }
        return true;
    }
}