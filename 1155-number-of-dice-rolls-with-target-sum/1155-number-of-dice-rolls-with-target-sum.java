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
        int[][] memo = new int[n + 1][target + 1];
        memo[0][0] = 1;
        for(int diceIndex = 1; diceIndex < n + 1; diceIndex++)
            for(int remainingSum = 1; remainingSum < target + 1; remainingSum++){
                for(int choice = 1; choice <= Math.min(k, remainingSum); choice++){
                    memo[diceIndex][remainingSum] = (memo[diceIndex][remainingSum]+memo[diceIndex - 1][remainingSum - choice])%MODULO;
                }
            }
        return memo[n][target];
        
        
        
    }
}