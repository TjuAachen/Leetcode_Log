class Solution {
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        //bfs
        LinkedList<LinkedList<Integer>> queue = new LinkedList<>();
        
        int source = 0;
        int end = graph.length - 1;
        queue.addLast(new LinkedList<>(Arrays.asList(source)));
        List<List<Integer>> ans = new LinkedList<>();
        
        
        
        while (!queue.isEmpty()) {
            LinkedList<Integer> poppedList = queue.pollFirst();
            int routeEnd = poppedList.peekLast();
            
            if (routeEnd == end) {
                ans.add(poppedList);
            }
            
            for (int nxt : graph[routeEnd]) {
                LinkedList<Integer> nxtList = new LinkedList<>(poppedList);
                nxtList.add(nxt);
                queue.add(nxtList);
            }
        }
        
        return ans;
        
    }
}