class Solution {
    public int jump(int[] nums) {
        int stepCount = 0;
        int curFarthest = 0;
        int jumpEnd = 0;
        for(int i = 0; i < nums.length ; i++){
            curFarthest = Math.max(curFarthest, nums[i] + i);
            if(jumpEnd == i){
                if (jumpEnd == nums.length - 1)return stepCount;
                stepCount += 1;
                jumpEnd = curFarthest;
            }
        }
        return stepCount;
    }
}