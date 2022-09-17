class Solution {
    LinkedList<Integer> temp = new LinkedList<>();
    List<List<Integer>> res  = new LinkedList<>();
    Set<Integer> visited = new HashSet<>();

    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        subset(nums, 0);
        return res;        
    }
    
    public void subset(int[] nums, int start){
        res.add((List) temp.clone());
        
        for(int i = start; i < nums.length; i++){
            int curNum = nums[i];
            if(i > 0 && nums[i-1] == nums[i] && !visited.contains(i-1))continue;
            visited.add(i);
            temp.addLast(curNum);
            subset(nums, i + 1);
            temp.pollLast();
            visited.remove(i);
        }
    }
    
}
