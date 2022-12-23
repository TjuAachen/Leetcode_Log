class Solution {
    public int[] sumOfDistancesInTree(int n, int[][] edges) {
        //input : n, edges
        //output : array of sum of distances
        //breaking down the problem:
        //1. set 0 as the root, bfs to traverse all the nodes
        //in one bfs traversal, the parent of one node is recorded and the number of nodes under one node as the root is saved.
        //Also, calculate the sum of distances from 0
        if (n == 1)
            return new int[n];
        
        int[] distances = new int[n];
        Map<Integer, Integer> parent = new HashMap<>();
        Map<Integer, Integer> numNodes = new HashMap<>();
        Map<Integer, List<Integer>> graph = new HashMap<>();

        buildGraph(graph, parent, edges);
        numNode(numNodes, parent, graph, 0, new HashSet<Integer>());
        
        //bfs
        LinkedList<Integer> queue = new LinkedList<>();
        queue.addLast(0);
        int step = 0;
        Set<Integer> visited = new HashSet<>();
        visited.add(0);
        
        while(!queue.isEmpty()){
            int size = queue.size();
            for (int i = 0; i < size; i++){
                int popped = queue.pollFirst();
                distances[0] += step;
                
                for (int nxt : graph.get(popped)){
                    if (visited.contains(nxt))
                        continue;
                    visited.add(nxt);
                    queue.addLast(nxt);
                }
            }
            step++;
            
        }
        
        //bfs traversal for the second time
        visited = new HashSet<>();
        queue = new LinkedList<>();
        queue.addLast(0);
        visited.add(0);
        
        while(!queue.isEmpty()){
            int parentNode = queue.pollFirst();
            for (int nxt : graph.get(parentNode)){
                if (visited.contains(nxt))
                    continue;
                visited.add(nxt);
                distances[nxt] = distances[parentNode] + n - 2 * numNodes.get(nxt);
                queue.addLast(nxt);
            }
        }
        
        return distances;
        
        
        
    }
    public void buildGraph(Map<Integer, List<Integer>> graph, Map<Integer, Integer> parent, int[][] edges){
        for (int[] edge : edges){
            Arrays.sort(edge);
            int start = edge[0];
            int end = edge[1];
            graph.computeIfAbsent(start, k -> new LinkedList<Integer>());
            graph.computeIfAbsent(end, k -> new LinkedList<Integer>());
            graph.get(start).add(end);
            graph.get(end).add(start);
          //  parent.put(end, start);
        }
    }
    public int numNode(Map<Integer, Integer> numNodes, Map<Integer, Integer> parent, Map<Integer, List<Integer>> graph, int root, Set<Integer> visited){
        
        visited.add(root);
        
        int ans = 1;
        
        for (int nxt : graph.get(root)){
            if (visited.contains(nxt))
                continue;
            ans += numNode(numNodes, parent, graph, nxt, visited);
            parent.put(nxt, root);
        }
        
        numNodes.put(root, ans);
        
        return ans;
    }
    
}