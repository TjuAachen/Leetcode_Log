class Solution {
    int MOD = (int) Math.pow(10, 9) + 7;
    public int concatenatedBinary(int n) {
        int res = 0;
        for(int i = 1; i < n + 1; i++){
            res = moveToLeft(res, numOfBits(i))%MOD + i%MOD ;
            res = res%MOD;
        }
        return res%MOD;
    }
    public int moveToLeft(int res, int num){
        while(num > 0){
            res = (res<<1)%MOD;
            num--;
        }
        return res;
        
        
        
    }
    public int numOfBits(int n){
        int ans = 0;
        while(n != 0){
            ans += 1;
            n = n>>1;
        }
        return ans;
    }
    
    
}