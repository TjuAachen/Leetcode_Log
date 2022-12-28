class Solution {
    public int minStoneSum(int[] piles, int k) {
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> (b - a));
        
        for (int pile : piles){
            pq.add(pile);
        }
        
        while(k > 0){
            int popped = pq.poll();
            popped -= Math.floor(popped / 2);
            pq.add(popped);
            k--;
        }
        
        int ans = 0;
        while(!pq.isEmpty()){
            ans += pq.poll();
        }
        
        return ans;
        
    }
}