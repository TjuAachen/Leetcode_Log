class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        HashMap<Integer, List<int[]>> graph = new HashMap<>();
        HashMap<Integer, int[]> dist = new HashMap<>();
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
        
        //construct graph
        for(int[] flight : flights){
            int cur_start = flight[0], cur_end = flight[1], cur_price = flight[2];
            graph.computeIfAbsent(cur_start, x -> new ArrayList<>()).add(new int[]{cur_end, cur_price});
        }
        


     //   dist.put(src, new int[]{0, 0});
        pq.offer(new int[]{0, 0, src});
        
        while(!pq.isEmpty()){
            
            int[] cur_flight = pq.poll();
            int temp_dist = cur_flight[0], temp_stop = cur_flight[1], temp_src = cur_flight[2];
            //traverse
            if(!dist.containsKey(temp_src) ||temp_dist < dist.get(temp_src)[0]){
                dist.put(temp_src, new int[]{temp_dist, temp_stop});
                if (temp_src == dst) return temp_dist;
            }
        
            for(int[] edge : graph.getOrDefault(temp_src, new ArrayList<>())){
                int end = edge[0], price = edge[1];
                //int[] end_val = dist.get(end);
                int num = 0;
                
                if (!dist.containsKey(end) && temp_stop <= k){
                   // dist.put(end, new int[]{price + temp_dist, temp_stop + 1});
                    pq.offer(new int[]{price + temp_dist, temp_stop + 1, end});
                }else if (dist.containsKey(end) && temp_stop < dist.get(end)[1]){
                    pq.offer(new int[]{price + temp_dist, temp_stop + 1, end});
                }  
            }
               
        }
        if (dist.containsKey(dst)){
            return dist.get(dst)[0];
        }
        return -1;
        
           
    }
}