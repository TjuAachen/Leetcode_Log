class Solution {
    public int divide(int dividend, int divisor) {
        int sign = 1;
        if(dividend < 0) sign =-sign;
        if(divisor < 0) sign = -sign;
        
        if(dividend > 0)dividend = -dividend;
        if(divisor > 0) divisor = -divisor;
        
        if(sign == 1 && dividend == Integer.MIN_VALUE && divisor == -1)return Integer.MAX_VALUE;
        int ans = this.helper(dividend, divisor);
        return ans * sign;
        
    }
    public int helper(int dividend, int divisor){
        int ans = 0;
        int temp_divisor = 0;
        int quotient = 0;
        while(dividend <= divisor){
            temp_divisor = divisor;
            quotient = 0;
            while(temp_divisor + temp_divisor >= dividend&& temp_divisor >= 0xc0000000){
                temp_divisor += temp_divisor;
                quotient += 1;
            }
            
            dividend -= temp_divisor;
            ans += (1<<quotient);
        }
        
        return ans;
        
        
        
        
    }

    
}