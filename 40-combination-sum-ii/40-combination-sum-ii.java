class Solution {
    private List<List<Integer>> list = new LinkedList<>();
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        Set<Integer> visited = new HashSet<>();
        combination(candidates, 0, 0, new LinkedList(), target, visited);
        return list;
    }
    public void combination(int[] candidates, int start, int curSum, LinkedList<Integer> curRes, int target, Set visited){
        if(curSum > target)return;
        if(curSum == target){
            list.add((List) curRes.clone());
            
        }
        
        for(int i = start; i < candidates.length; i++){
            if(i > start && candidates[i-1] == candidates[i]&&!visited.contains(i-1))continue;
            curRes.add(candidates[i]);
            visited.add(i);
            combination(candidates, i + 1, curSum + candidates[i], curRes, target, visited);
            curRes.pollLast();
            visited.remove(i);
        }
        
    }
}