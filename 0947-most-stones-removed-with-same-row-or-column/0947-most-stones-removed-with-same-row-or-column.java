class Solution {
    Map<Integer, List<Integer>> adj = new HashMap<>();
    boolean[] visited;
    
    public int removeStones(int[][] stones) {
        
        buildGraph(stones, adj);
        
        int n = stones.length;
        
        int connectedComponentNum = 0;
        
        visited = new boolean[n];
        
        
        
        for(int i = 0; i < n; i++){
            
            if(!visited[i]){
                visitAllConnectedNodes(visited, i, adj);
                connectedComponentNum++;
            }
        }
        
        return n - connectedComponentNum;
    }
    
    public void visitAllConnectedNodes(boolean[] visited, int src, Map<Integer, List<Integer>> adj){
        
        visited[src] = true;
        
        for(int nxt : adj.get(src)){
            
            if(!visited[nxt]){
                visitAllConnectedNodes(visited, nxt, adj);
            }
        }  
    }
    
    
    public void buildGraph(int[][] stones, Map<Integer, List<Integer>> adj){
        
        int n = stones.length;
        
        for(int i = 0; i < n; i++){
            int prevRow = stones[i][0];
            int prevCol = stones[i][1];
            adj.computeIfAbsent(i, k->new LinkedList<Integer>());
            for(int j = i + 1; j < n; j++){
                int row = stones[j][0];
                int col = stones[j][1];
                adj.computeIfAbsent(j, k->new LinkedList<Integer>());
                if(prevRow != row && prevCol != col)
                    continue;
                adj.get(j).add(i);
                adj.get(i).add(j);
            }
    
        }
    
    }
    
    
}
