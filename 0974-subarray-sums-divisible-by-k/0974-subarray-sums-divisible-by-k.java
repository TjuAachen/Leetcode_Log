class Solution {
    public int subarraysDivByK(int[] nums, int k) {
        int n = nums.length;
        int[] prefix = new int[n + 1];
        Map<Integer, Integer> remainderCount = new HashMap<>();
        int ans = 0;
        
        for (int i = 1; i < n + 1; i++) {
            prefix[i] = prefix[i - 1] + nums[i - 1];
            int curRemainder = prefix[i] % k;
            remainderCount.computeIfAbsent(curRemainder, key -> 0);
            if (remainderCount.containsKey(curRemainder))
                ans += remainderCount.get(curRemainder);
            if (remainderCount.containsKey(curRemainder - k))
                ans += remainderCount.get(curRemainder - k);
            if (remainderCount.containsKey(curRemainder + k))
                ans += remainderCount.get(curRemainder + k);
            
            if (curRemainder == 0)
                ans += 1;
            remainderCount.put(curRemainder, remainderCount.get(curRemainder) + 1);
            int target = k - curRemainder;
        }
        
        return ans;
        
        
        
        
    }
}