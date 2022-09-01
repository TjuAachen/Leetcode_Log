class Solution {
  //  private HashMap<Pair, Boolean> memo = new HashMap<>();
    private HashMap<Integer, Integer> distToInd = new HashMap<>();
    public boolean canCross(int[] stones) {
        if(stones[1] > 1)return false;
        int N = stones.length;
        boolean res = false;
        

        distToInd.put(0, 0);
        boolean[][] dp = new boolean[N][N];
        dp[0][0] = true;
        for(int position = 1; position < N; position++){
            int real_dist = stones[position];
            distToInd.put(real_dist, position);
            for(int step = 1; step <= Math.min(real_dist, N - 1); step++){
                if(distToInd.containsKey(real_dist - step)){
                    int new_idx = distToInd.get(real_dist - step);
                    
                    dp[position][step] |= dp[new_idx][step];
                    if (step + 1 < N)
                        dp[position][step] |= dp[new_idx][step+1];
                    if(step - 1 >= 0)
                        dp[position][step] |= dp[new_idx][step-1];
                    }
                if(position == N - 1)
                    res |= dp[position][step];
            }
        }
        return res;
        
    }

}