class Solution {
    public int threeSumClosest(int[] nums, int target) {
        Arrays.sort(nums);
        int N = nums.length;
        int ans = 300000;
        for(int i = 0; i < N - 2; i++){
            int cur_num = nums[i];
            int newTarget = target - cur_num;
            int cur_res = this.twoSumClosest(i + 1, nums, newTarget);
            if (Math.abs(cur_res + cur_num - target) < Math.abs(ans - target)){
                ans = cur_res + cur_num;
            }
            if (ans == target) return target;
                
        }
        return ans;
        
    }
    public int twoSumClosest(int start, int[] nums, int target){
        int N = nums.length;
        int left = start, right = N - 1;
        int res = 300000;
        while(left < right){
            int cur_sum = nums[left] + nums[right];
            if (Math.abs(res - target) > Math.abs(cur_sum - target)){
                res = cur_sum;
            }
            if (cur_sum == target) return target;
            if (cur_sum < target)
                left++;
            if (cur_sum > target)
                right--;
            
        }
        return res;
        
    }
}