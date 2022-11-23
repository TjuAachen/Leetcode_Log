
class Solution {
    public int trapRainWater(int[][] heightMap) {
        //1D two pointer, boundary comparison
        //move the lower one
        //break down problem:
        //1.add all bounary points into the heap
        //2.pop up the lowest
        //3.find all unvisited neighbors, add into the result and update heap.
        
        int nRow = heightMap.length;
        int nCol = heightMap[0].length;
        
        int res = 0;
        
        PriorityQueue<int[]> pq = new PriorityQueue<>( (a, b) ->(a[2] - b[2]) );
        Set<Pair<Integer, Integer>> visited = new HashSet<>();
        
        for(int row = 0; row < nRow; row++){
            //row, 0, heightMap[row][0]
            //row, nCol - 1, heightMap[row][nCol - 1]
            pq.add(new int[]{row, 0, heightMap[row][0]});
            pq.add(new int[]{row, nCol - 1, heightMap[row][nCol - 1]});
            
            Pair<Integer, Integer> key1 = new Pair(row, 0);
            Pair<Integer, Integer> key2 = new Pair(row, nCol - 1);
            visited.add(key1);
            visited.add(key2);
        }
            
        for(int col = 0; col < nCol; col++){
            //0, col, heightMap[0][col]
            //nRow - 1, col, heightMap[nRow - 1][col]
            pq.add(new int[]{0, col, heightMap[0][col]});
            pq.add(new int[]{nRow - 1, col, heightMap[nRow - 1][col]});
            
            Pair<Integer, Integer> key1 = new Pair(0, col);
            Pair<Integer, Integer> key2 = new Pair(nRow - 1, col);
            visited.add(key1);
            visited.add(key2);
            
        }
        
        int[][] dirs = new int[][]{{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        
        
        
        while(!pq.isEmpty()){
            
            int[] cell = pq.poll();
            
            for(int[] dir : dirs){
                int newRow = cell[0] + dir[0];
                int newCol = cell[1] + dir[1];
                Pair<Integer, Integer> newKey = new Pair(newRow, newCol);
                if(newRow < 0 || newRow >= nRow || newCol < 0 || newCol >= nCol || visited.contains(newKey))
                    continue;
                
                res += Math.max(0, cell[2] - heightMap[newRow][newCol]);
                pq.add(new int[]{newRow, newCol, Math.max(cell[2], heightMap[newRow][newCol])});
                visited.add(newKey);
            }
        }
        
        return res;
        
    }
}