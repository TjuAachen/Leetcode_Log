class Solution {
    public int largestVariance(String s) {
        int res = 0;
        for(int i = 0; i < 26; i++)
            for(int j = 0; j < 26; j++){
                char char1 = (char)(i + 'a');
                char char2 = (char)(j + 'a');
                if(char1 == char2){
                    continue;
                }
                for(int round = 0; round < 2; round++){
                    int freq1 = 0;
                    int freq2 = 0;
                    for(int k = 0; k < s.length(); k++){
                        char curChar = s.charAt(k);
                        if(curChar != char1 && curChar != char2){
                            continue;
                        }
                        if(curChar == char1)freq1++;
                        if(curChar == char2)freq2++;
                        if(freq1 < freq2){
                            freq1 = 0;
                            freq2 = 0;
                        }else if(freq1 > 0 && freq2 > 0){
                            res = Math.max(res, freq1 - freq2);
                        }
                    }
                    StringBuilder m = new StringBuilder();
                    m.append(s);
                    m.reverse();
                    s = m.toString();
                }
            }
        return res;
    }
    
}