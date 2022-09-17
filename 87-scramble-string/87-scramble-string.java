class Solution {
    Map<String, Boolean> memo = new HashMap<>();
    public boolean isScramble(String s1, String s2) {
        if(s1.length() <= 1){
            return s1.equals(s2);
        }
        String key = s1 + "#" + s2;
        if(memo.containsKey(key))return memo.get(key);
        int s1Len = s1.length();
        for(int i = 1; i < s1.length(); i++){
            boolean curRes = false;
            String s1Sub1 = s1.substring(0, i), s1Sub2 = s1.substring(i);
            String s2Sub1 = s2.substring(0, i), s2Sub2 = s2.substring(i);
            String s2Sub1Changed = s2.substring(0, s1Len - i), s2Sub2Changed = s2.substring(s1Len - i);
            //if not exchange
            curRes |=isScramble(s1Sub1, s2Sub1) && isScramble(s1Sub2, s2Sub2);
            if (curRes){
                memo.put(key, true);
                return true;
            }
            //if exchange
            curRes |=isScramble(s1Sub1, s2Sub2Changed) && isScramble(s1Sub2, s2Sub1Changed);
            if (curRes){
                memo.put(key, true);
                return true;
            }
        }
        memo.put(key, false);
        return false;
    }
}