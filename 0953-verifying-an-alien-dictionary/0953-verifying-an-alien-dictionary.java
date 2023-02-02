class Solution {
    public boolean isAlienSorted(String[] words, String order) {
        int[] charToOrder = new int[26];
        for (int i = 0; i < 26; i++) {
            char curChar = order.charAt(i);
            charToOrder[curChar - 'a'] = i;
        }
        
        int n = words.length;
        
        for (int j = 0; j < n - 1; j++) {
            String cur = words[j];
            String nxt = words[j + 1];
            int curLength = cur.length();
            int nxtLength = nxt.length();
            int minLength = Math.min(cur.length(), nxt.length());
            
            for (int k = 0; k < minLength; k++) {
                int curCharIdx = cur.charAt(k) - 'a';
                int nxtCharIdx = nxt.charAt(k) - 'a';
                int curCharOrder = charToOrder[curCharIdx];
                int nxtCharOrder = charToOrder[nxtCharIdx];
                if (curCharOrder > nxtCharOrder)
                    return false;
                else if (curCharOrder < nxtCharOrder)
                    break;
            }
            if (cur.substring(0, minLength).equals(nxt.substring(0, minLength)) && minLength == nxtLength && curLength > nxtLength)
                return false;
        }
        
        return true;
        
    }
}