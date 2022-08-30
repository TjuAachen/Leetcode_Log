class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        Arrays.sort(nums);
        List<List<Integer>> ans = this.findKSum(0, nums, (long) target, 4);
        return ans;
        
        
    }
    public List<List<Integer>> findKSum(int start, int[] nums, long target, int K){
        int N = nums.length;
        List<List<Integer>> ans = new ArrayList<>();
        if (K > 2){
            int i = start;
            while(i < N - K + 1){
                int cur_num = nums[i];
                if((long)cur_num * K > target) return ans;
                long newTarget = target - cur_num;
                List<List<Integer>> temp_res = this.findKSum(i+1, nums, newTarget, K - 1);
                if (!temp_res.isEmpty()){
                    for(List<Integer> cur : temp_res){
                        cur.add(cur_num);
                        ans.add(cur);
                    }
                }
                
                while(i < N - K + 1 && nums[i] == cur_num) i++;    
            }
            
        }else{
            int left = start, right = N - 1;
            long cur_res = 0;
            while(left < right){
                cur_res = nums[left] + nums[right];
                int cur_left = nums[left], cur_right = nums[right];
                if(cur_res == target){
                    ans.add(new ArrayList<Integer>(Arrays.asList(nums[left], nums[right])));
                    while(left < right && nums[left] == cur_left) left++;
                    while(right > left && nums[right] == cur_right) right--;
                }else if(cur_res < target){
                    while(left < right && nums[left] == cur_left) left++;
                }else{
                    while(right > left && nums[right] == cur_right) right--;
                }
                
                
            }
            
        }
        return ans;
    }
    

}

