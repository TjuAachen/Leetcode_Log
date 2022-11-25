class Solution {
    public int sumSubarrayMins(int[] arr) {
        int MOD = 1000000007;
        
        LinkedList<int[]> incStack = new LinkedList<>();
        
        int length = arr.length;
        
        long ans = 0;
        
        for(int i = 0; i < length + 1; i++){
            int curVal = Integer.MIN_VALUE;
             if(i < length){
            curVal = arr[i];
            }
            while(!incStack.isEmpty() && incStack.peekLast()[0] > curVal){
                int[] popped = incStack.pollLast();
                int left = -1;
                if(!incStack.isEmpty()){
                    left = incStack.peekLast()[1];
                }
                int midIndex = popped[1];
                int right = i;
                long temp = ((right - midIndex) * (midIndex - left))%MOD;
                long tempProduct = (temp * popped[0])%MOD;
                ans += tempProduct;
                ans %= MOD;
            }
            incStack.add(new int[]{curVal, i});
        }
        
        return (int) ans%MOD;
        
    }
}