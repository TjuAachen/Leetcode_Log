class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        //@input : gas/cost from i to i + 1
        //@output : the starting position such that it can go through all the elements
        //@edge case : integer limit, negative number
        //@breaking down problem:
        //1. calculate the difference
        //2. calculate the prefix sum for the differences
        //3. traverse the difference and calcu
        //注意此时有解且唯一，说明满足条件即可,相减和大于等于0，说明必有解
        int n = gas.length;
        int[] diff = new int[n];
        int sum = 0;
        int curStreak = 0;
        int ans = 0;
        for(int i = 0; i < n; i++){
            diff[i] = gas[i] - cost[i];
            curStreak += diff[i];
            if(curStreak < 0){
                curStreak = 0;
                ans = i + 1;
            }
            sum += diff[i];
        }
        if(sum < 0)return -1;
        return ans;
        
        
        
        
        
    }
}