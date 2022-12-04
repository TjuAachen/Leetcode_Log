class Solution {
    public int minimumAverageDifference(int[] nums) {
        int n = nums.length;
        long[] prefix = new long[n + 1];
        
        
        for (int i = 1; i <= n; i++){
            prefix[i] = prefix[i - 1] + (long) nums[i - 1];

            
        }
        
        int res = Integer.MAX_VALUE;
        int idx = 0;
        
        for (int j = 0; j < n; j++){
            int firstAverage =Math.round(prefix[j + 1] / (j + 1));
            int secondAverage = 0;
            if (n - j - 1 != 0){
            secondAverage =Math.round((prefix[n] - prefix[j + 1]) / (n - j - 1));
            }
            if (Math.abs(firstAverage - secondAverage) < res){
                res = Math.abs(firstAverage - secondAverage);
                idx = j;
            }
            
        }
        
        return idx;
    }
}