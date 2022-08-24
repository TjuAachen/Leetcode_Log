class Solution {
    public int lengthOfLongestSubstring(String s) {
        int N = s.length();
        int left = 0, right = 0;
        int ans = 0;
        //sliding window + rolling hash
        HashSet<Character> freq = new HashSet<Character>();
        while(right < N){
            while(left < right && freq.contains(s.charAt(right))) {
                freq.remove(s.charAt(left++));
            }
            //right expand
            freq.add(s.charAt(right++));
            ans = Math.max(ans, freq.size());
        }
        return ans;
    }
}