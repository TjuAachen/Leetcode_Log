class Solution {
    private List<List<Integer>> res = new LinkedList<>();
    private LinkedList<Integer> temp = new LinkedList<>();
    private int start = 0;
    public List<List<Integer>> subsets(int[] nums) {
        res.add((List) temp.clone());
        for(int i = start; i < nums.length; i++){
            start = i + 1;
            temp.addLast(nums[i]);
            subsets(nums);
            temp.pollLast();
        }
        return res;
    }
}