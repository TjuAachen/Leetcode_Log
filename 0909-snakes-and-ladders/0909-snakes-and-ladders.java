class Solution {
    public int snakesAndLadders(int[][] board) {
        //bfs + visited
        int n = board.length;
        int dest = n * n;
        LinkedList<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        int step = 0;
        
        Map<Integer, Pair<Integer, Integer>> val2Idx = new HashMap<>();
        buildMapFromVal2Idx(n, val2Idx);
        
        //bfs
        queue.add(1);
        while (!queue.isEmpty()) {
            int size = queue.size();
            for (int i = 0; i < size; i++) {
                int popped = queue.pollFirst();
                if (visited.contains(popped))
                    continue;
                visited.add(popped);
                if (popped == dest)
                    return step;
                //nxt
              //  System.out.printf("%d %d\n",step, popped);
                
                for (int nxt = popped + 1; nxt < Math.min(popped + 7, dest + 1); nxt++) {

                    Pair<Integer, Integer> idx = val2Idx.get(nxt);
                    
                    //decide whether it is snake or ladder
                    int curVal = board[idx.getKey()][idx.getValue()];
                  //  System.out.printf("%d %d %d %d\n", popped, nxt, curVal, step);
                    if (curVal == -1) {
                        queue.addLast(nxt);
                    }else{
                        if (!visited.contains(curVal)) {
                            queue.addLast(curVal); 
                        }
                    }
                    
                }
            }
            step += 1;
        }
        
        return -1;

    }
    
    public void buildMapFromVal2Idx(int n, Map<Integer, Pair<Integer, Integer>> val2Idx) {
        int label = 1;
        Integer[] columns = new Integer[n];
        
        for (int i = 0; i < n; i++) {
            columns[i] = i;
        }
        
        for (int row = n - 1; row >= 0; row--) {
            for (int column : columns) {
                val2Idx.put(label++, new Pair<>(row, column));
            }
            Collections.reverse(Arrays.asList(columns));
        }
    }
    

}