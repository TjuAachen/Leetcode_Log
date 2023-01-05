class Solution {
    public int findMinArrowShots(int[][] points) {

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0]? a[0] - b[0] : -a[1] + b[1]);
        PriorityQueue<int[]> enterQueue = new PriorityQueue<>((a, b) -> a[0] != b[0]? a[0] - b[0] : a[1] - b[1]);
        Map<Pair, Boolean> isBursted = new HashMap<>();
        //sweep line
        for (int[] point : points){
            int[] enter = new int[]{point[0], 1, point[1]};
            int[] leave = new int[]{point[1], -1, point[0]};
            pq.add(enter);
            pq.add(leave);
        }
        
        int ans = 0;
        while(!pq.isEmpty()){
            int[] popped = pq.poll();
            //if it is enter
            if (popped[1] == 1){
                enterQueue.add(popped);
                continue;
            }
            Pair<Integer, Integer> key = new Pair<>(popped[2], popped[0]);
            if (isBursted.containsKey(key) && isBursted.get(key))
                continue;
            //burst all ballons in enter queue
            while(!enterQueue.isEmpty()){
                int[] enterPopped = enterQueue.poll();
                Pair<Integer, Integer> newKey = new Pair<>(enterPopped[0], enterPopped[2]);
                isBursted.put(newKey, true);
            }
            ans += 1;
            
        }
        
        return ans;
        
    }
}