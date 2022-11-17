class unionSet{
    
    int[] size;
    int[] parent;
    public unionSet(int n){
        
        size = new int[n];
        parent = new int[n];
        
        for(int i = 0; i < n; i++){
            parent[i] = i;
            size[i] = 1;
        }
    }
    
    public int find(int node){
        
        if(node == parent[node])
            return node;
        
        parent[node] = find(parent[node]);
        
        return parent[node];
    }
    
    public void union(int p, int q){
        
        int parentP = find(p);
        int parentQ = find(q);
        
        if(parentP == parentQ)
            return;
        
        if(size[parentP] <= size[parentQ]){
            size[parentQ] += size[parentP];
            parent[parentP] = parentQ;
        }else{
            size[parentP] += size[parentQ];
            parent[parentQ] = parentP;
        }
    }
    
}
class Solution {
    public int findCircleNum(int[][] isConnected) {
        
        int n = isConnected.length;
        
        unionSet set = new unionSet(n);
        
        for(int i = 0; i < n; i++)
            for(int j = i + 1; j < n; j++){
                
                if(isConnected[i][j] == 1){
                    set.union(i, j);
                }
            }
        
        Set<Integer> visited = new HashSet<>();
        
        for(int k = 0; k < n; k++){
            
            int curParent = set.find(k);
            if(!visited.contains(curParent)){
                visited.add(curParent);
            }
        }
        
        return visited.size();
        
        
        
        
        
        
    }
}