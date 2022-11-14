class unionFind{
    
    int[] parent;
    int[] size;
    public unionFind(int n){
        
        //initialization
        parent = new int[n];
        size = new int[n];
        for(int i = 0; i < n; i++){
            parent[i] = i;
            size[i] = 1;
        }

    }
    
    public void union(int p, int q){
        
        int parentP = find(p);
        int parentQ = find(q);
        
        if(parentP == parentQ)
            return;
        
        if(size[parentP] <= size[parentQ]){
            parent[parentP] = parentQ;
            size[parentQ] += size[parentP];
        }else{
            parent[parentQ] = parentP;
            size[parentP] += size[parentQ];            
        }
    }
    
    public int find(int p){
        
        if(p == parent[p])
            return p;
        
        parent[p] = find(parent[p]);
        return parent[p];
    }
}


class Solution {
    public int removeStones(int[][] stones) {
        
        //construct the union find
        int numStone = stones.length;
        
        unionFind unionSet = new unionFind(numStone);
        
        for(int i = 0; i < numStone; i++){
            int prevRow = stones[i][0];
            int prevCol = stones[i][1];
            for(int j = i + 1; j < numStone; j++){
                int curRow = stones[j][0];
                int curCol = stones[j][1];
                
                if(prevRow == curRow || prevCol == curCol){
                    unionSet.union(i, j);
                }
            }
        }
        
        
        int ans = 0;
        Set<Integer> addedParent = new HashSet<>();
        
        
        for(int k = 0; k < numStone; k++){
            
            int curParent = unionSet.find(k);
            if(!addedParent.contains(curParent)){
                addedParent.add(curParent);
            }
        }
        
        return numStone - addedParent.size();
        
        
        
        
        
        
        
        
    }
}