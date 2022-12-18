class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
        LinkedList<int[]> monoStack = new LinkedList<>();
        int n = temperatures.length;
        int[] res = new int[n];
        
        for (int i = 0; i < n; i++){
            int curTemp = temperatures[i];
            
            while(!monoStack.isEmpty() && monoStack.getLast()[1] < curTemp){
                int[] popped = monoStack.pollLast();
                res[popped[0]] = i - popped[0];
                
            }
            monoStack.addLast(new int[]{i, curTemp});
        }
        
        return res;
        
    }
}