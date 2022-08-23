class Solution {
    public String longestPalindrome(String s) {
        //expand around center
        int N = s.length();
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < N; i++){
            helper(s, i, 0, sb);
            helper(s, i, 1, sb);
        }
        return sb.toString();
        
        
        }
    private void helper(String s, int center, int offset, StringBuilder sb){
        int left = center, right = center + offset;
        int N = s.length();
        while(left >= 0 && right < N && s.charAt(left) == s.charAt(right)){
            left--;
            right++;
        }
        String cur = s.substring(left+1, right); //[i,j)
        if (cur.length() > sb.length()){
            sb.setLength(0);
            sb.append(cur);
        }
        
    }
}