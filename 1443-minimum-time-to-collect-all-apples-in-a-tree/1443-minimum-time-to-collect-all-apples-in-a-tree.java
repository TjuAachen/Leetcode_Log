class Solution {
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        //input : int[][] edges
        //output : minTime to take all apples
        //break down problem: sub-problem
        //minTime of leftChild + minTime of rightChild
        //if either child is an apple, then add 2
        Map<Integer, List<Integer>> graph = new HashMap<>();
        buildGraph(n, edges, graph);
        
        int res = findMin(0, -1, edges, graph, hasApple);
        
        return Math.max(res, 0);
    }
    
    public void buildGraph(int n, int[][] edges, Map<Integer, List<Integer>> graph) {
        for (int curNode = 0; curNode < n; curNode++) {
            graph.put(curNode, new LinkedList<Integer>());
        }
        
        for (int[] edge : edges){
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }
    }
    
    public int findMin(int curNode, int parentNode, int[][] edges, Map<Integer, List<Integer>> graph, List<Boolean> hasApple) {
        int  ans = 0;
        for (int nxt : graph.get(curNode)) {
            if (nxt == parentNode)
                continue;
            int nxtMin = findMin(nxt, curNode, edges, graph, hasApple);
            if (nxtMin != -1)
                ans += (nxtMin + 2);
        }
        
        if (ans == 0 && !hasApple.get(curNode))
            return -1;
        return ans;
    }
    
}