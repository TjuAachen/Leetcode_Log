class Solution {
    private Set<Integer> visited = new HashSet<>();
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> res = new LinkedList<>();
        
        permuteRes(nums, res, new LinkedList<>());
        return res;
    }
    
    public void permuteRes(int[] nums, List res, LinkedList temp){
        if (temp.size() == nums.length){
            res.add((List) temp.clone());
            return;
        }
        for(int i = 0; i < nums.length; i++){
            if(visited.contains(i))continue;
            visited.add(i);
            temp.addLast(nums[i]);
            permuteRes(nums, res, temp);
            temp.pollLast();
            visited.remove(i);
        }
        
        
        
        
    }
}