class Solution {
    public long minimumFuelCost(int[][] roads, int seats) {
        //dfs from the leaf node to the root
        Map<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(roads, graph);
        
        return dfs(0, -1, seats, graph)[2];
        
        
        
    }
    
    public long[] dfs(int node, int parent, int seats, Map<Integer, List<Integer>> graph) {
        long[] res = new long[]{1, 1, 0};

        if (!graph.containsKey(node))
            return res;
        for (int nxt : graph.get(node)) {
            if (nxt == parent)
                continue;
            long[] nxtRes = dfs(nxt, node, seats, graph);
            res[0] += nxtRes[0];
            res[1] += nxtRes[1];
            res[2] += nxtRes[2] + nxtRes[0];
        }
        
        //combine

        res[0] = (long) Math.min(res[1] / seats + (res[1] % seats == 0? 0 : 1), res[0]);
     //   System.out.printf("%d %d %d %d\n", node, res[0], res[1], res[2]);
        return res;
        
    }
    
    
    
    public void buildGraph(int[][] roads, Map<Integer, List<Integer>> graph) {
        for (int[] road : roads) {
            int start = road[0];
            int end = road[1];
            
            graph.computeIfAbsent(start, k -> new LinkedList<Integer>());
            graph.computeIfAbsent(end, k -> new LinkedList<Integer>());
            
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
    }
}