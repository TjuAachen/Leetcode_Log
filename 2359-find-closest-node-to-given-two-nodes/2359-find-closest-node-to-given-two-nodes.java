class Solution {
    public int closestMeetingNode(int[] edges, int node1, int node2) {
        Map<Integer, Integer> dist1 = new HashMap<>();
        Map<Integer, Integer> dist2 = new HashMap<>();
        int n = edges.length;
        longestDist(edges, node1, dist1);
        longestDist(edges, node2, dist2);
        
        int ans = Integer.MAX_VALUE;
        int ansIdx = -1;
        
        for (int i = 0; i < n; i++) {
            int val1 = -1;
            int val2 = -1;
            if (dist1.containsKey(i))
                val1 = dist1.get(i);
            if (dist2.containsKey(i))
                val2 = dist2.get(i); 
            
            if (val1 != -1 && val2 != -1) {
                if (ans > Math.max(val1, val2)) {
                    ans = Math.max(val1, val2);
                    ansIdx = i;
                }
                    
            }
        }
        
        return ansIdx;
        
    }
    public void longestDist(int[] edges, int node, Map<Integer, Integer> distance) {
        ArrayList<Integer> queue = new ArrayList<>();
        queue.add(node);
        distance.put(node, 0);
        
        while (!queue.isEmpty()) {
            int popped = queue.remove(0);
            int curDist = distance.get(popped);
            
            //nxt
            int nxt = edges[popped];
            if (nxt != -1 && (!distance.containsKey(nxt) || distance.get(nxt) > curDist + 1)) {
                queue.add(nxt);
                distance.put(nxt, curDist + 1);
            }
        }
    }
}