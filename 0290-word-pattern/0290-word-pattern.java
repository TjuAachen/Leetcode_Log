class Solution {
    public boolean wordPattern(String pattern, String s) {
        String[] arrOfStr = s.split(" ");
        int patternLen = pattern.length();
        int arrOfStrLen = arrOfStr.length;
        
        if (patternLen != arrOfStrLen)
            return false;
        Map<Character, String> pattern2Str = new HashMap<>();
        Map<String, Character> str2Pattern = new HashMap<>();
        
        for (int curPatternIdx = 0; curPatternIdx < patternLen; curPatternIdx++){
            char curChar = pattern.charAt(curPatternIdx);
            if (pattern2Str.containsKey(curChar)){
                if (!pattern2Str.get(curChar).equals(arrOfStr[curPatternIdx])){
                    return false;
                }
            }else{
                pattern2Str.put(curChar, arrOfStr[curPatternIdx]);
            }
            
            if (str2Pattern.containsKey(arrOfStr[curPatternIdx])){
                if (!str2Pattern.get(arrOfStr[curPatternIdx]).equals(curChar)){
                    return false;
                }
            }else{
                str2Pattern.put(arrOfStr[curPatternIdx], curChar);
            }
            
        }
        
        return true;
    }

}