class Solution {
    public String longestPalindrome(String s) {
        int N = s.length();
        boolean[][] dp = new boolean[N][N];
        //base case:
        //odd: dp[i][i] = true, even: dp[i][i+1] = true, 
        //transition equation:
        //if s.charAt[i] == s.charAt[j] && j - i >= 2: dp[i][j] = dp[i+1][j-1]
        //elif j - i < 2, dp[i][j] = true
        int start = 0, end = 0;
        for (int i = N - 1; i >= 0; i--)
            for(int j = i; j < N; j++)
                if (s.charAt(i) == s.charAt(j) && (j - i <= 2 || dp[i+1][j-1])){
                    dp[i][j] = true;
                    if (j - i > end - start){
                        start = i;
                        end = j;
                    }
                }
        return s.substring(start, end + 1);
        }
}