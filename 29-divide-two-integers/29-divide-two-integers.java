class Solution {
    public int divide(int dividend, int divisor) {
        if (dividend == 0x80000000 && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        int negative = 2;
        if (dividend > 0) {
            dividend = -dividend;
            negative--;
        }
        if (divisor > 0) {
            negative--;
            divisor = -divisor;
        }
        
        int result = divideCore(dividend, divisor);
        return negative == 1? -result : result;
        
        
    }
    private int divideCore(int dividend, int divisor) {
        int ans = 0;
        while (dividend <= divisor) {
            int value = divisor;
            int quotient = 1;
            while (value >= 0xc0000000 && value + value >= dividend) {
                value += value;
                quotient += quotient;
            }
            dividend -= value;
            ans += quotient;
        }
        return ans;
    }
    
}