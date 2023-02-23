class Solution {
    public int findMaximizedCapital(int k, int w, int[] profits, int[] capital) {
       // pure profit, greedy
        //profit, capital
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] != b[0]? b[0] - a[0] : a[1] - b[1]);
        //order by capital
        int n = profits.length;
        int[][] profitCapital = new int[n][2];
        
        for (int i = 0; i < n; i++) {
            profitCapital[i][0] = profits[i];
            profitCapital[i][1] = capital[i];
        }
        
        Arrays.sort(profitCapital, (a, b) -> a[1] != b[1]? a[1] - b[1] : a[0] - b[0]);
        
        int p = 0;
        
        while (p < n && profitCapital[p][1] <= w) {
            pq.add(profitCapital[p]);
            p++;
        }
        
        
        while (k > 0 && !pq.isEmpty()) {
            //add all satisfying capital profit pair into the pq
            //pop the first one
            int[] popped = pq.poll();
            w += popped[0];
            
            while (p < n && profitCapital[p][1] <= w) {
                pq.add(profitCapital[p]);
                p++;
            }
            
            k -= 1;
        }
        
        return w;
        
        
    }
}