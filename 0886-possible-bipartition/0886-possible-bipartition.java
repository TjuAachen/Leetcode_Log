class Solution {
    public boolean possibleBipartition(int n, int[][] dislikes) {
        Map<Integer, Integer> groupId = new HashMap<>();
        Map<Integer, List<Integer>> graph = new HashMap<>();
        
        for (int[] dislike : dislikes){
            int left = dislike[0];
            int right = dislike[1];
            
            graph.computeIfAbsent(left, k -> new LinkedList<Integer>());
            graph.computeIfAbsent(right, k -> new LinkedList<Integer>());
            
            graph.get(left).add(right);
            graph.get(right).add(left);    
        }
        
        for (int i = 1; i <= n; i++){
            if (!graph.containsKey(i))
                continue;
            if (groupId.containsKey(i))
                continue;
            //bfs
            LinkedList<Integer> queue = new LinkedList<>();
            queue.addLast(i);
            groupId.put(i, -1);
            
            while(!queue.isEmpty()){
                int size = queue.size();
                for (int j = 0; j < size; j++){
                    int popped = queue.pollFirst();

                    for (int nxt : graph.get(popped)){
                        if (groupId.containsKey(nxt) && groupId.get(nxt) == groupId.get(popped)){
                            return false;
                        }
                        if (groupId.containsKey(nxt))
                            continue;
                        groupId.put(nxt, -groupId.get(popped));
                        queue.addLast(nxt);
                    }
                    
                }
            }
        }
        
        
        
        return true;
        
        
        
    }
}