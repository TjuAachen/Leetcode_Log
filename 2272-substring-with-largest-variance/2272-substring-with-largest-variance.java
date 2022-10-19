class Solution {
    public int largestVariance(String s) {
        int res = 0;
        Map<Character, Integer> counter = new HashMap<>();
        for(int m = 0; m < s.length(); m++){
            counter.computeIfAbsent(s.charAt(m), k -> 0);
            counter.put(s.charAt(m), counter.get(s.charAt(m)) + 1);
        }
        
        
        for(int i = 0; i < 26; i++)
            for(int j = 0; j < 26; j++){
                char char1 = (char)(i + 'a');
                char char2 = (char)(j + 'a');
                if(char1 == char2){
                    continue;
                }
                if(!counter.containsKey(char2) | !counter.containsKey(char1))continue;
                int freq1 = 0;
                int freq2 = 0;
                
                int remainingChar2 = counter.get(char2);
                for(int k = 0; k < s.length(); k++){
                    char curChar = s.charAt(k);
                    if(curChar != char1 && curChar != char2){
                        continue;
                    }
                    if(curChar == char1)freq1++;
                    if(curChar == char2){
                        freq2++;
                        remainingChar2--;
                    }
                    if(freq1 < freq2 && remainingChar2 > 0){
                        freq1 = 0;
                        freq2 = 0;
                    }else if(freq1 > 0 && freq2 > 0){
                        res = Math.max(res, freq1 - freq2);
                    }
                }
            }
            
        return res;
    }
    
}