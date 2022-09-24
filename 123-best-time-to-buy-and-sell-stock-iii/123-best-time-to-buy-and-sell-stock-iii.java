class Solution {
    public int maxProfit(int[] prices) {
    //@input: prices + at most two transactions//是否需要特殊处理，有无越界可能
    //@output: maximum profit
    //@edge case : no
    //@steps:
    //in unified way
        
    int t1Cost = Integer.MAX_VALUE, t2Cost = Integer.MAX_VALUE;
    int t1Profit = 0, t2Profit = 0;
    for(int price : prices){
        t1Cost = Math.min(t1Cost, price);
        t1Profit = Math.max(t1Profit, price - t1Cost);
        //reinvent
        t2Cost = Math.min(t2Cost, price - t1Profit);
        t2Profit = Math.max(t2Profit, price - t2Cost);
    }
        return t2Profit;
    }
}