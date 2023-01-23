class Solution {
    public List<List<String>> partition(String s) {
        //@input : string s
        //@output: all possible palindrome partitioning of s
        //@edge case : no
        //@breaking down problem:
        // 1. backtracking
        // 2. if come to the end, then terminate
        // 3. in each step, select the palindrome one
        List<List<String>> res = new LinkedList<>();
        List<String> temp = new LinkedList<>();
        int n = s.length();
        boolean[][] dp = new boolean[n][n];
        backtracking(s, 0, res, temp, dp);
        return res;
        
        
        
    }

    public void backtracking(String s, int curPointer, List<List<String>> res, List<String> temp, boolean[][] dp){
        //termination
        
        if(curPointer == s.length()){
            res.add(new LinkedList<>(temp));
            return;
        }
        for(int i = curPointer; i < s.length(); i++){
            //select
            String curPartition = s.substring(curPointer, i + 1);
            if (s.charAt(curPointer) == s.charAt(i) && (i - curPointer <= 2 || dp[curPointer + 1][i - 1])) {
                dp[curPointer][i] = true;
                temp.add(curPartition);
                backtracking(s, i + 1, res, temp, dp);
                temp.remove(temp.size() - 1);
            }
            
        }
    }
    
    
}