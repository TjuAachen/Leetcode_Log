class Solution {
    public int longestPath(int[] parent, String s) {
        int n = s.length();
        int[] longestLen = new int[n];
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        buildGraph(parent, n, graph);
        
        return maxAns(0, graph, longestLen, s);
        
    }
    
    public void buildGraph(int[] parent, int n, Map<Integer, List<Integer>> graph) {
        for (int node = 0; node < n; node++) {
            graph.put(node, new LinkedList<>());
        }
        
        for (int node = 1; node < n; node++) {
            graph.get(parent[node]).add(node);
        }
    }
    
    
    public int maxAns(int curNode, Map<Integer, List<Integer>> graph, int[] singleLongest, String s) {
        char curChar = s.charAt(curNode);

        singleLongest[curNode] = 1;
        int max1 = 0, max2 = 0;
        int ans = 1;
        
        for (int nxtNode : graph.get(curNode)) {

            ans = Math.max(ans, maxAns(nxtNode, graph, singleLongest, s));
            char nxtChar = s.charAt(nxtNode);
            if (curChar == nxtChar)
                continue;
            
            singleLongest[curNode] = Math.max(singleLongest[curNode], singleLongest[nxtNode] + 1);
            
            if (max1 == 0) {
                max1 = singleLongest[nxtNode];
            }else if (max1 < singleLongest[nxtNode]) {
                max2 = max1;
                max1 = singleLongest[nxtNode];
            }else 
                max2 = Math.max(max2, singleLongest[nxtNode]);  
        }

        ans = Math.max(ans, max1 + max2 + 1);
        
        return ans;
    }
}