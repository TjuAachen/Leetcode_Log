class Solution {
    public int compress(char[] chars) {

        int charsLen = chars.length;
        char prevChar = '1';
        int res = 0;
        int count = 0;
        int j = 0;
        
        for (int i = 0; i < charsLen + 1; i++) {
            char curChar = '0';
            
            if (i < charsLen)
                curChar = chars[i];
            
            if (curChar == prevChar) {
                count += 1;
            }else {
                if (count == 1) {
                    res += 1;
                    chars[j++] = prevChar;
                }else if (count != 0){
                    res = res + 1 + ("" + count).length();
                    String countStr = "" + count;
                    chars[j++] = prevChar;
                    
                    for (int k = 0; k < countStr.length(); k++) {
                        chars[j++] = countStr.charAt(k);
                    }
                }
                prevChar = curChar;
                count = 1;
            }
        }

        return res;
    }
}