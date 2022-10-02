class Solution {
    Map<String, Integer> memo = new HashMap<>();
    int MODULO = 1000000007;
    public int numRollsToTarget(int n, int k, int target) {
        //@input : n dice and k faces from 1 to k, target
        //@output : number of ways to get the target
        //@edge case : large integer, modulo 10^9 + 7
        //@breaking down the problem:
        //1. permutation with repeatition + memo
        //2. recursion. 
        //2.1 In each recursion, if in memo, return
        //2.2 if target == 0, return 1
        //2.3 if target < 0, return 0
        //3. select from 1 to k, 
        if(target == 0){
            if(n == 0)return 1;
            return 0;
        }
        if(target > k * n)return 0;
        if(target == k * n)return 1;
        if(target < 0)return 0;
        String key = String.valueOf(n) + "#" + String.valueOf(k) + "#" + String.valueOf(target);
        if(memo.containsKey(key))return memo.get(key);
        int curRes = 0;
        for(int nxt = 1; nxt < k + 1; nxt++){
            if(target < nxt)continue;
            curRes += numRollsToTarget(n - 1, k, target - nxt);
            curRes = curRes%MODULO;
        }
        memo.put(key, curRes%MODULO);
        return curRes%MODULO;
        
        
        
        
        
    }
}