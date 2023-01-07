class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        //@input: gas, cost
        //@output: the gas station's index if you can travel around circuit
        //breaking down the problem:
        //1.starting from the first element
        //2.1 if it works, then gas no less than cost
        //2.2 if not, then go to the nxt station as a new index
        int startIndex = 0;
        int gasCum = 0;
        
        for (int idx = 0; idx < gas.length; idx++){
            int curGas = gas[idx];
            int curCost = cost[idx];
            if (gasCum + curGas < curCost){
                startIndex = idx + 1;
                gasCum = 0;
                continue;
            }
            gasCum += curGas - curCost;
        }
        if (isFeasible(startIndex, gas, cost))
            return startIndex;
        return -1;
    }
    
    public boolean isFeasible(int startIdx, int[] gas, int[] cost){
        
        int gasCum = 0;
        int totalNum = gas.length;
        
        if (startIdx >= totalNum)
            return false;
        
        for (int step = 0; step < totalNum; step++){
            int curIdx = (step + startIdx)%totalNum;
            int curGas = gas[curIdx];
            int curCost = cost[curIdx];
            if (gasCum + curGas < curCost)
                return false;
            gasCum += curGas - curCost;
        }
        return true;
        
        
        
    }
    
}