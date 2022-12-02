class Solution {
    public boolean closeStrings(String word1, String word2) {
        //不为0的字母相同
        //不为0的字母的occurrences种类相同
        int[] word1Freq = new int[26];
        int[] word2Freq = new int[26];
        Set<Character> charInWord1 = new HashSet<>();
        Set<Character> charInWord2 = new HashSet<>();
        
        
        int word1Len = word1.length();
        int word2Len = word2.length();
        
        if(word1Len != word2Len)
            return false;
        
        
        for(int i = 0; i < word1Len; i++){
            char curChar1 = word1.charAt(i);
            char curChar2 = word2.charAt(i);
            
            charInWord1.add(curChar1);
            charInWord2.add(curChar2);
            
            word1Freq[curChar1 - 'a'] += 1;
            word2Freq[curChar2 - 'a'] += 1;
        }
        
        for(Character word1Char : charInWord1){
            if(!charInWord2.contains(word1Char))
                return false;
        }
        
        Arrays.sort(word1Freq);
        Arrays.sort(word2Freq);
        
        for(int j = 0; j < 26; j++){
            if(word1Freq[j] != word2Freq[j])
                return false;
        }
        
        return true;
        
        
        
    }
}