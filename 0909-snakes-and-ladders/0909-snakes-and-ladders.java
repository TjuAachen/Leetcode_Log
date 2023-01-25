class Solution {
    public int snakesAndLadders(int[][] board) {
        //bfs + distance
        Map<Integer, Integer> distance = new HashMap<>();
        ArrayList<Integer> queue = new ArrayList<>();
        Map<Integer, Pair<Integer, Integer>> val2Idx = new HashMap<>();
        int n = board.length;
        int dest = n * n;
        
        buildMapFromVal2Idx(n, val2Idx);
        
        //bfs
        queue.add(1);
        distance.put(1, 0);
        while (!queue.isEmpty()) {
            int popped = queue.remove(0);
            int curDist = distance.get(popped);
            
            for (int nxt = popped + 1; nxt <= Math.min(dest, popped + 6); nxt++) {
                Pair<Integer, Integer> idx = val2Idx.get(nxt);
                int curVal = board[idx.getKey()][idx.getValue()];
                //if curVal = -1, add directly
                if (curVal == -1 && (!distance.containsKey(nxt) || distance.get(nxt) > curDist + 1)) {
                    distance.put(nxt, curDist + 1);
                    queue.add(nxt);
                } else if (curVal != -1 && (!distance.containsKey(curVal) || distance.get(curVal) > curDist + 1)) {
                    distance.put(curVal, curDist + 1);
                    queue.add(curVal);                    
                }
            } 
        }
        
        if (!distance.containsKey(dest))
            return -1;
        return distance.get(dest);

    }
    
    public void buildMapFromVal2Idx(int n, Map<Integer, Pair<Integer, Integer>> val2Idx) {
        int label = 1;
        Integer[] columns = new Integer[n];

        
        for (int i = 0; i < n; i++) {
            columns[i] = i;
        }
        
        for (int row = n - 1; row >= 0; row--) {
            for (int column : columns) {
                val2Idx.put(label++, new Pair(row, column));                
            }
            Collections.reverse(Arrays.asList(columns));
            
        }
        
    }
    

}