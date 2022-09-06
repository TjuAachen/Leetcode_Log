class Solution {
    private List<List<Integer>> res = new LinkedList<>();
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        
        findSum(candidates, 0, 0, new LinkedList<>(), target);
        return res;
    }
    public void findSum(int[] candidates, int start, int tempSum, LinkedList<Integer> tempRes, int target){
        if(tempSum > target)return;
        if(tempSum == target){
            res.add((List) tempRes.clone());
            return;
        }
        for(int i = start; i < candidates.length; i++){
            int curVal = candidates[i];
            tempRes.addLast(curVal);
            findSum(candidates, i, tempSum + curVal, tempRes, target);
            tempRes.pollLast();
        }
    }
    
}