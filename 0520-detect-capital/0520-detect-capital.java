class Solution {
    public boolean detectCapitalUse(String word) {
        int capitalPos = -1;
        int wordLen = word.length();
        int capitalNum = 0;
        
        for (int idx = 0; idx < wordLen; idx++){
            char curChar = word.charAt(idx);
            if (Character.isUpperCase(curChar)){
                capitalPos = idx;
                capitalNum++;
            }
        }
        if (capitalNum == 0 || wordLen == capitalNum)
            return true;
        if (capitalNum == 1 && capitalPos == 0)
            return true;
        return false;
        
        
    }
}