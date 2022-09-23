class Solution {
    int MOD = (int) Math.pow(10, 9) + 7;
    public int concatenatedBinary(int n) {
        long res = 0;
        int length = 0;
        for(int i = 1; i < n + 1; i++){
            if ((i & (i - 1)) == 0) {
                length++;
            }
            res = ((res << length) | i)%MOD;

        }
        return (int)res;
    }


    
    
}