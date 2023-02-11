class Solution {
    public int maxDistance(int[][] grid) {
        //bfs from all land cells to find the maximum minimum dist from land
        Map<Pair<Integer, Integer>, Integer> distance = new HashMap<>();
        int nRow = grid.length;
        int nCol = grid[0].length;
        ArrayList<int[]> queue = new ArrayList<>();
        int[][] nxtMoves = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (int row = 0; row < nRow; row++)
            for (int col = 0; col < nCol; col++) {
                int curCellVal = grid[row][col];
                Pair<Integer, Integer> point = new Pair<>(row, col);
                int[] queueElement = new int[]{row, col, 0};
                //if cell val is 1
                if (curCellVal == 1) {
                    queue.add(queueElement);
                } else {
                    distance.put(point, Integer.MAX_VALUE);
                }
            }
        
        while (!queue.isEmpty()) {
            int[] popped = queue.get(0);
            queue.remove(0);
            
            for (int[] nxtMove : nxtMoves) {
                int nxtX = popped[0] + nxtMove[0];
                int nxtY = popped[1] + nxtMove[1];
                if (nxtX < nRow && nxtX >= 0 && nxtY < nCol && nxtY >= 0 && grid[nxtX][nxtY] == 0) {
                    Pair<Integer, Integer> nxtPoint = new Pair<>(nxtX, nxtY);
                    if (distance.get(nxtPoint) > popped[2] + 1) {
                        distance.put(nxtPoint, popped[2] + 1);
                        queue.add(new int[]{nxtX, nxtY, popped[2] + 1});
                    }
                }
            }
        }
        
        int res = 0;
        for (Map.Entry<Pair<Integer, Integer>, Integer> entry: distance.entrySet()) {
            res = Math.max(entry.getValue(), res);
        }
        
        if (res == Integer.MAX_VALUE || res == 0)
            return -1;
        return res;
    }
}