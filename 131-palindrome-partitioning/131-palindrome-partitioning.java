class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> res = new ArrayList<>();
        //find all palindromic substring
        int N = s.length();
        boolean[][] dp = new boolean[N][N];
        for(int i = N - 1; i >= 0; i--)
            for(int j = i; j < N; j++)
                if(s.charAt(i) == s.charAt(j) &&(j - i <= 2 || dp[i+1][j-1])){
                    dp[i][j] = true;
                }
        backtracking(s, 0, new ArrayList<>(), res, dp);
        return res;
        
    }
    private void backtracking(String s, int pos, List<String> temp, List<List<String>> res, boolean[][] dp){
        if(pos == s.length()){
            res.add(new ArrayList<>(temp));
            return;
        }
        for(int i = pos; i < s.length(); i ++)
            if (dp[pos][i]){
                temp.add(s.substring(pos, i + 1));
                backtracking(s, i + 1, temp, res, dp);
                temp.remove(temp.size() - 1);
            }
    }
}