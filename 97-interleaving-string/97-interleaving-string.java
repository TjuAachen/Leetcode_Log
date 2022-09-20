class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        int n = s1.length(), m = s2.length();
        boolean[][] dp = new boolean[n + 1][m + 1];
        if(n + m != s3.length())return false;
        
        dp[0][0] = true;
        char s1Char;
        char s2Char;
        char target;
        for(int i = 0; i < n + 1; i++)
            for(int j = 0; j < m + 1; j++){
                if(i == 0 && j == 0)continue;

                dp[i][j] = false;
                target = s3.charAt(i+j-1);
                if(i == 0){
                    s2Char = s2.charAt(j-1);
                    dp[i][j] = dp[i][j-1] &&s2Char == target;
                    continue;
                }
                s1Char = s1.charAt(i-1);
                if(j == 0){
                    dp[i][j] = dp[i-1][j] && s1Char == target;
                    continue;
                }
                s2Char = s2.charAt(j-1);
                if(s1Char == target){
                    dp[i][j]  |= dp[i-1][j];
                }
                if(s2Char == target){
                    dp[i][j] |= dp[i][j-1];
                }
             //   System.out.printf("%d %d\n", i, j);
           //     System.out.println(dp[i][j]);
            }
       // System.out.println(dp[2][0]);
        return dp[n][m];
        
    }
}