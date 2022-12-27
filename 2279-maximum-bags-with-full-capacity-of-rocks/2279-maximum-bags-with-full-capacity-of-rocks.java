class Solution {
    public int maximumBags(int[] capacity, int[] rocks, int additionalRocks) {
        int n = capacity.length;
        int[] diff = new int[n];
        
        for (int i = 0; i < n; i++){
            diff[i] = capacity[i] - rocks[i];
        }
        
        Arrays.sort(diff);
        int ans = 0;
        
        for (int j = 0; j < n; j++){
            if (additionalRocks >= diff[j]){
                ans++;
                additionalRocks -= diff[j];
            }
        }
        
        return ans;
        
        
    }
}