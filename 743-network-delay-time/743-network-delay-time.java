class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        HashMap<Integer, Integer> dist = new HashMap<>();
        HashMap<Integer, List<int[]>> graph = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> (a[0] - b[0]));
        
        //construct graph
        for(int[] edge : times){
            int source = edge[0], end = edge[1], weight = edge[2];
            graph.computeIfAbsent(source, x -> new ArrayList<>()).add(new int[]{end, weight});
        }
        
        pq.offer(new int[]{0, k});
        int res = 0;
        while(!pq.isEmpty()){
            int [] min_temp = pq.poll();
            int temp_dist = min_temp[0], start = min_temp[1];
            if (dist.containsKey(start)) continue;
            dist.put(start, temp_dist);
            res = Math.max(res, temp_dist);
           // System.out.println(dist);
            //traverse all its neighbors
            for(int[] nei : graph.getOrDefault(start, new ArrayList<>())){
                int center = nei[0], center_dist = nei[1];
                if (!dist.containsKey(center)){
                    pq.offer(new int[]{center_dist + temp_dist, center});
                }
            }
            
            
        }
        if (dist.size() == n) return res;
        return -1;
}
}