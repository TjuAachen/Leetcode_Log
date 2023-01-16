class Solution {
    int[] size;
    int[] parent;
    public int find(int node) {
        if (node == parent[node])
            return node;
        parent[node] = find(parent[node]);
        return parent[node];
    }
    public int numberOfGoodPaths(int[] vals, int[][] edges) {
        int n = vals.length;
        int ans = n;
        Map<Integer, List<Integer>> graph = new HashMap<>();
        //start from the minimum vals
        int[][] valIdx = new int[n][2];
        
        for (int idx = 0; idx < n; idx++) {
            valIdx[idx][0] = vals[idx];
            valIdx[idx][1] = idx;
        }
        Arrays.sort(valIdx, (a, b) -> a[0] - b[0]);
        buildGraph(edges, n, graph);
        //size is num of maxVal in the union
        size = new int[n];
        parent = new int[n];
        
        for (int idx = 0; idx < n; idx++) {
            parent[idx] = idx;
            size[idx] = 1;
        }
        
        for (int idx = 0; idx < n; idx++) {
            int curVal = valIdx[idx][0];
            int realIdx = valIdx[idx][1];
            int curParent = find(realIdx);
            
            for (int nxt : graph.get(realIdx)) {
                int nxtVal = vals[nxt];
                int nxtParent = find(nxt);
                
                if (nxtParent == curParent || nxtVal > curVal)
                    continue;
                if (vals[nxtParent] == curVal) {
                    ans += size[nxtParent] * size[curParent];
                    size[curParent] += size[nxtParent];
                }
                parent[nxtParent] = curParent;

            }
        }
        
        return ans;

    }
    
    public void buildGraph(int[][] edges, int n, Map<Integer, List<Integer>> graph) {
        for (int idx = 0; idx < n; idx++) {
            graph.put(idx, new LinkedList<>());
        }
        
        for (int[] edge : edges) {
            int start = edge[0], end = edge[1];
            graph.get(start).add(end);
            graph.get(end).add(start);
        }
    }

}