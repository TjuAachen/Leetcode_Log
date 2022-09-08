class Solution {
    private Set<Integer> visited = new HashSet<>();
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new LinkedList<>();
        permuteRes(nums, res, new LinkedList<>());
        return res;
    }
    
    public void permuteRes(int[] nums, List res, LinkedList temp){
        if(temp.size() == nums.length){
            res.add((List) temp.clone());
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(visited.contains(i)) continue;
            if(i > 0 && nums[i] == nums[i-1] && !visited.contains(i-1))continue;
            visited.add(i);
            temp.addLast(nums[i]);
            permuteRes(nums, res, temp);
            visited.remove(i);
            temp.pollLast();
        }
        
        
        
        
    }
}