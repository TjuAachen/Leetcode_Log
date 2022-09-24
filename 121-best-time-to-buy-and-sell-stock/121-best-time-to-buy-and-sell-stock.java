class Solution {
    public int maxProfit(int[] prices) {
        //input: the prices data in each data
        //output: the maximum profit can gain
        //edge case : no
        //1. traverse from 0 to the end
        //2. find the minimum value up to now, and calculate the profit up to now
        int ans = 0;
        int min = Integer.MAX_VALUE;
        for(int i = 0; i < prices.length; i++){
            min = Math.min(prices[i], min);
            ans = Math.max(ans, prices[i] - min);
        }
        return ans;
    }
}