class Solution {
    public int maxProfit(int[] prices) {
        int N = prices.length;
        int min = prices[0];
        int profit = 0;
        for(int i = 1; i < N; i++){
            profit = Math.max(prices[i] - min, profit);
            min = Math.min(prices[i], min);
        }
        return profit;
    }
}