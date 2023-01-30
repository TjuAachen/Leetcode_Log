class Solution {
    public int tribonacci(int n) {
        int ans = 0;
        int first = 0;
        int second = 1;
        int third = 1;
        
        if (n == 0) {
            return 0;
        }
        if (n == 1) {
            return 1;
        }
        if (n == 2) {
            return 1;
        }
        
        for (int i = 3; i < n + 1; i++) {
            ans = first + second + third;
            first = second;
            second = third;
            third = ans;
        }
        
        return ans;
    }
}