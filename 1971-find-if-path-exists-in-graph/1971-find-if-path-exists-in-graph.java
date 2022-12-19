class Solution {
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        if (source == destination)
            return true;
      //build graph
        HashMap<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(edges, graph);
    // bfs
        Set<Integer> visited = new HashSet<>();
        LinkedList<Integer> queue = new LinkedList<>();
        queue.addLast(source);
        visited.add(source);
        
        while(!queue.isEmpty()){
            int popped = queue.pollFirst();
            
            //nxt node
            if (!graph.containsKey(popped))
                continue;
            for (int nxt : graph.get(popped)){
                if (nxt == destination)
                    return true;
                if (visited.contains(nxt))
                    continue;
                visited.add(nxt);
                queue.addLast(nxt);
            }
        }
        
        return false;
        
        
        
        
    }
    public void buildGraph(int[][] edges, HashMap<Integer, List<Integer>> graph){
        
        for (int[] edge : edges){
            int start = edge[0];
            int end = edge[1];
            
            graph.computeIfAbsent(start, k -> new LinkedList<Integer>());
            graph.computeIfAbsent(end, k -> new LinkedList<Integer>());
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
        
        
        
    }
}