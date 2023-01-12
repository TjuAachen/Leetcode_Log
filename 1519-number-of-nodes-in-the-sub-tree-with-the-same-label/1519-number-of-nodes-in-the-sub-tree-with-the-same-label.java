class Solution {
    public int[] countSubTrees(int n, int[][] edges, String labels) {
        int[][] dp = new int[n][26];
        int[] ans = new int[n];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        buildGraph(graph, edges, n);
        
        // dfs
        dfs(graph, 0, -1, n, labels, ans, dp);
        
        return ans;
    }
    
    public void buildGraph(Map<Integer, List<Integer>> graph, int[][] edges, int n) {
        for (int node = 0; node < n; node++) {
            graph.put(node, new LinkedList<Integer>());
        }
        for (int[] edge : edges) {
            int node1 = edge[0], node2 = edge[1];
            graph.get(node1).add(node2);
            graph.get(node2).add(node1);
        }
    }
    
    public void dfs(Map<Integer, List<Integer>> graph, int curNode, int parent, int n, String labels, int[] ans, int[][] dp) {
        //add the node's curVal to dp
        char curChar = labels.charAt(curNode);
        int charIdx = curChar - 'a';
        dp[curNode][charIdx] = 1;
        for (int nxt : graph.get(curNode)) {
            if (nxt == parent)
                continue;

            dfs(graph, nxt, curNode, n, labels, ans, dp);
            
            for (int nxtIdx = 0; nxtIdx < 26; nxtIdx++)
                dp[curNode][nxtIdx] += dp[nxt][nxtIdx];
        }
        
        ans[curNode] = dp[curNode][charIdx];
    }
}