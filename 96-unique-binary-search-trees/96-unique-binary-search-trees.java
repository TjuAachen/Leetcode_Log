class Solution {
    Map<Pair, Integer> memo = new HashMap<>();
    public int numTrees(int n) {
        return numSubTrees(1, n);
    }
    
    public int numSubTrees(int start, int end){
        if(start > end)return 1;
        int res = 0;
        Pair key = new Pair(start, end);
        if(memo.containsKey(key))return memo.get(key);
        
        for(int i = start; i < end + 1; i++){
            int leftNum = numSubTrees(start, i - 1);
            int rightNum = numSubTrees(i + 1, end);
            res += (leftNum * rightNum);
        }
        memo.put(key, res);
        return res;
    }
}