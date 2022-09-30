class Solution {
    public int singleNumber(int[] nums) {
        int[] bits = new int[32];
        for(int num : nums){
            int[] tempBits = findBits(num);
            addBits(bits, tempBits);
        }
        int ans = 0;
        for(int i = 0; i < bits.length; i++){
            //System.out.println(bits[i]);
            if(bits[i] % 3 != 0){
                ans += 1<<i;
            }
        }
        return ans;
        
        
        
        
        
        
    }
    public int[] findBits(int num){
        int[] bits = new int[32];
        
        for(int i = 0; i < 32; i++){
            int mask = 1<<i;
            if((num & mask) != 0){
                bits[i] = 1;
            }
        }
        return bits;
    }
    public void addBits(int[] targetBits, int[] bits){
        for(int i = 0; i < targetBits.length; i++){
            targetBits[i] += bits[i];
        }
    }
    
}