class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        HashMap<Integer, List<int[]>> graph = new HashMap<Integer, List<int[]>>();
        for (int[] edge : times)
            graph.computeIfAbsent(edge[0], x -> new ArrayList<>()).add(new int[]{edge[1], edge[2]});
        PriorityQueue<int[]> pq = new PriorityQueue<int []>((a, b) -> (a[0] - b[0]));
        Map<Integer, Integer> dist = new HashMap<>();
        pq.offer(new int[]{0, k});
        int res = 0;
        while(!pq.isEmpty()){
            //extract min
            int[] u = pq.poll();
            int cur_dist = u[0], cur_source = u[1];
            if (dist.containsKey(cur_source)) continue;
            dist.put(cur_source, cur_dist);
            res = Math.max(res, cur_dist);
            //traverse all the neighbors still in queue
            for(int[] edge : graph.getOrDefault(cur_source, new ArrayList<>())){
                int nei = edge[0], distance2 = edge[1];
                if (!dist.containsKey(nei))
                    pq.offer(new int[]{distance2 + cur_dist, nei});
                
            }
            
        }
        
        if (dist.size() != n) return -1;
        return res;
    }
}