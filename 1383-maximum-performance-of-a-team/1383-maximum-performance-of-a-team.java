class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        int MOD =(int) Math.pow(10,9) + 7;
        ArrayList<int[]> array = new ArrayList<>();
        PriorityQueue<Integer> pq = new PriorityQueue<>((a, b) -> a - b);
        
        //pair speed with efficiency
        for(int i = 0; i < speed.length; i++){
            int curSpeed = speed[i];
            int curEfficiency = efficiency[i];
            array.add(new int[]{curSpeed, curEfficiency});
        }
        //sort efficiency in decreasing order
        Collections.sort(array, (o1,o2) ->o2[1] - o1[1]);
        
        
        long speedSum = 0;
        long ans = 0;
        int s = 0, e = 0;
        for(int j = 0; j < array.size(); j++){
            s = array.get(j)[0];
            e = array.get(j)[1];
            if(pq.size() > k - 1){
                speedSum -= pq.remove();
            }
            pq.add(s);
            speedSum += s;
            ans = Math.max(ans, speedSum * e);
        }
        return (int)(ans%MOD);
    
    }
}