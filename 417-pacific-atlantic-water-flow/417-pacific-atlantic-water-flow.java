class Solution {
    private int nrow;
    private int ncol;
    private int[][] directions = new int[][]{{1,0},{-1,0},{0,1},{0,-1}};
    private int[][] heights;
    private  Queue<int[]> pacific = new LinkedList<>();
    private Queue<int[]> atlantic = new LinkedList<>();
    public List<List<Integer>> pacificAtlantic(int[][] heights) {

        nrow = heights.length; ncol = heights[0].length;
        
        boolean[][] pacificReachable = new boolean[nrow][ncol];
        boolean[][] atlanticReachable = new boolean[nrow][ncol];
        this.heights = heights;
        this.initialization();
        this.bfs(pacific, pacificReachable);
        this.bfs(atlantic, atlanticReachable);
        
        List<List<Integer>> res = new LinkedList<>();
        for(int row = 0; row < nrow; row++)
            for(int col = 0; col < ncol; col++){
                if (pacificReachable[row][col] && atlanticReachable[row][col])res.add(Arrays.asList(row, col));
            }
        return res;
        

    

    }
    //initialization
    public void initialization(){
        for(int row = 0; row < nrow; row++){
            pacific.offer(new int[]{row,0});

            atlantic.offer(new int[]{row,ncol - 1});

        }
        for(int col = 0; col < ncol; col++){
            pacific.offer(new int[]{0,col});

            atlantic.offer(new int[]{nrow-1,col});

        }            
        
    }
    public void bfs(Queue<int[]> queue, boolean[][] Reachable){
        Set<Pair> visited = new HashSet<>();
        
        while(!queue.isEmpty()){
            int queue_size = queue.size();
            for(int i = 0; i < queue_size; i++){
                int[] idx = queue.poll();
                Pair idx_pair = new Pair(idx[0], idx[1]);
                visited.add(idx_pair);
                Reachable[idx[0]][idx[1]] = true;
                
                for(int[] direction : directions){
                    int dx = direction[0], dy = direction[1];
                    int newx = idx[0] + dx, newy = idx[1] + dy;
                    Pair new_pair = new Pair(newx, newy);
                    if(newx < nrow && newx >=0 && newy < ncol && newy >= 0 && heights[newx][newy] >= heights[idx[0]][idx[1]] && !visited.contains(new_pair)){
                        queue.offer(new int[]{newx, newy});
                        
                    }
                }
            }
        }
        
        
    }
}