class Solution {
    Map<String, Integer> memo = new HashMap<>();
    public int numDistinct(String s, String t) {
        //@input the string s
        //@output the num of distinct subsequences of the string s equal to string t
        
        //@breaking down
        //since only the number is needed, we can solve this problem by dynamic programming.
        //1.define the status variable
        //dp[i][j] -- the number of subsequences for s[i:] equal to t[j:]
        //2.recursion + memo
        //3.edge case
        int sLen = s.length(), tLen = t.length();
        String key = s + "#" + t;
        if(tLen == 0)return 1;
        if(tLen > sLen) return 0;
        if(tLen == sLen){
            if(t.equals(s))return 1;
            return 0;
        }
        if(memo.containsKey(key))return memo.get(key);
        //delete or not
        char firstS = s.charAt(0);
        char firstT = t.charAt(0);
        int temp1 = 0, temp2 = 0;
        if(firstS == firstT){
            temp1 = numDistinct(s.substring(1), t.substring(1));
        }
        temp2 = numDistinct(s.substring(1), t);
        memo.put(key, temp1 + temp2);
        return memo.get(key);
    }
}