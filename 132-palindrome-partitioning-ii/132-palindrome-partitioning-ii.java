class Solution {
    public int minCut(String s) {
        //@input : a string
        //@output : minimum cuts needed for a palindrome partitioning of s
        //@edge case : no
        //@breaking down problem:
        // 1. start from the end and cut from the longest palindrome
        // 2. when the longest palindrome is not the end, then ans + 1
        // 3. otherwise, return ans;
        int n = s.length();
        boolean[][] isPalindrome = new boolean[n][n];
        setPalindrome(s, isPalindrome);
        int endIdx = n - 1;
        int ans = 0;
        int[] min = new int[n];
        //只考虑min[n] minimum cut of [0, end]
        for(int end = 0; end < n; end++){
            int temp = end;
            for(int start = 0; start <= end; start++){
                if(isPalindrome[start][end]){
                    if(start == 0){
                        temp = 0;
                    }else{
                        temp = Math.min(min[start - 1] + 1, temp);
                    }
                }
            }
            min[end] = temp;
        }
        return min[n - 1];
        
        
        
        
        
        
        
    }
    public void setPalindrome(String s, boolean[][] dp){
        int n = s.length();
        
        for(int i = n - 1; i >= 0; i--)
            for(int j = i; j < n; j++){
                if(i == j){
                    dp[i][j] = true;
                    continue;
                }
                if(s.charAt(i) == s.charAt(j)){
                    if(j - i == 1){
                        dp[i][j] = true;
                    }else{
                    dp[i][j] = dp[i+1][j-1];
                    }
                }else{
                    dp[i][j] = false;
                }
            }
        
        
    }
    
    
    
}