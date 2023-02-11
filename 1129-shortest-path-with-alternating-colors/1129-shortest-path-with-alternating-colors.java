class Solution {
    public int[] shortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) {
        Map<Integer, List<Integer>> redGraph = new HashMap<>();
        Map<Integer, List<Integer>> blueGraph = new HashMap<>();
        
        buildGraph(redEdges, redGraph);
        buildGraph(blueEdges, blueGraph);
        
        ArrayList<int[]> queue = new ArrayList<>();
        //1- red, -1 - blue
        //{node, dist, red/blue}
        queue.add(new int[]{0, 0, -1});
        queue.add(new int[] {0, 0, 1});
        Map<Pair<Integer, Integer>, Integer> distance = new HashMap<>();
        distance.put(new Pair(0, 1), 0);
        while (!queue.isEmpty()) {
            int[] popped = queue.get(0);
            queue.remove(0);
            
            //if red
            Pair curPair = new Pair(popped[0], popped[2]);
            Map<Integer, List<Integer>> graph;
            if (popped[2] == 1) {
                graph = blueGraph;
            }else {
                graph = redGraph;
            }
            if (distance.containsKey(curPair) && distance.get(curPair) < popped[1])
                continue;
            distance.put(curPair, popped[1]);
            if (!graph.containsKey(popped[0]))
                continue;
            //nxt blue
            for (int nxt : graph.get(popped[0])) {
                Pair nxtPair = new Pair(nxt, -popped[2]);
                if (!distance.containsKey(nxtPair) || distance.get(nxtPair) > popped[1] + 1) {
                    distance.put(nxtPair, popped[1] + 1);
                   // System.out.printf("%d %d %d\n", nxt, -popped[2], popped[1] + 1);
                    int[] nxtPoint = new int[]{nxt, popped[1] + 1, -popped[2]};
                    queue.add(nxtPoint);
                }
            }
        }
        
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            Pair pairBlue = new Pair(i, -1);
            Pair pairRed = new Pair(i, 1);
            int redVal = Integer.MAX_VALUE;
            int blueVal = Integer.MAX_VALUE;
            
            if (distance.containsKey(pairBlue))
                blueVal = distance.get(pairBlue);
            if (distance.containsKey(pairRed))
                redVal = distance.get(pairRed);
            int curAns = Math.min(redVal, blueVal);
            if (curAns == Integer.MAX_VALUE)
                res[i] = -1;
            else
                res[i] = curAns;

        }
        
        return res;
        
        
        
        
        
    }
    
    public void buildGraph(int[][] edges, Map<Integer, List<Integer>> graph) {
        for (int[] edge : edges) {
            int start = edge[0];
            int end = edge[1];
            graph.computeIfAbsent(start, k -> new LinkedList<Integer>());
            graph.get(start).add(end);
        }
    }
}