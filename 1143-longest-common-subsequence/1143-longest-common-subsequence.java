class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int text1Length = text1.length();
        int text2Length = text2.length();
        
        int[][] longestCommon = new int[text1Length + 1][text2Length + 1];
        
        int ans = 0;
        
        for (int p1 = 1; p1 < text1Length + 1; p1++)
            for (int p2 = 1; p2 < text2Length + 1; p2++){
                char text1Char = text1.charAt(p1 - 1);
                char text2Char = text2.charAt(p2 - 1);
                
                if (text1Char == text2Char){
                    longestCommon[p1][p2] = Math.max(longestCommon[p1][p2], longestCommon[p1 - 1][p2 - 1] + 1);
                }else{
                    longestCommon[p1][p2] = Math.max(longestCommon[p1][p2], longestCommon[p1 - 1][p2]);
                    longestCommon[p1][p2] = Math.max(longestCommon[p1][p2], longestCommon[p1][p2 - 1]);
                }
                
                ans = Math.max(longestCommon[p1][p2], ans);
            }
        
        return ans;
    
    }
}