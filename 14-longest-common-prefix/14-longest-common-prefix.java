class Solution {
    public String longestCommonPrefix(String[] strs) {
        //common prefix cannot exceed the length of the first word
        int N = strs[0].length();
        for(int i = 0; i < N; i++){
            String nxt_prefix = strs[0].substring(0, i + 1);
            if (!this.isCommonPrefix(nxt_prefix, strs)) return strs[0].substring(0, i);
        }
        return strs[0];
        
    }
    public boolean isCommonPrefix(String str, String[] strs){
        int N = strs.length;
        int prefix_len = str.length();
        for(String elem : strs){
            if (prefix_len > elem.length()) return false;
            String cur_string = elem.substring(0, prefix_len);
            if(!cur_string.equals(str)) return false;
        }
        return true;
    }
}