class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int N = nums.length;
        int i = 0;
        List<List<Integer>> res = new LinkedList<>();
        Arrays.sort(nums);
        while(i < N){
            int first_num = nums[i];
            twoSumTarget(first_num, i + 1, -first_num, res, nums);
            while(i < N && nums[i] == first_num) i++;
            
            
        }
        
        return res;
    }
    public void twoSumTarget(int first_num, int idx, int target, List res, int[] nums){
        int N = nums.length;
        int left = idx, right = N - 1;
        
        //two pointer
        while(left < right){
            int temp = nums[left] + nums[right];
            int left_val = nums[left], right_val = nums[right];
            if (temp == target){
                List<Integer> cur_res = new LinkedList<>(Arrays.asList(first_num, nums[left], nums[right]));
                res.add(cur_res);
                while(left < right && nums[left] == left_val) left++;
                while(left < right && nums[right] == right_val) right--;
                
            }else if(temp < target){
                while(left < right && nums[left] == left_val) left++;
            }else{
                while(left < right && nums[right] == right_val) right--;
            }
        }
        
    }
}