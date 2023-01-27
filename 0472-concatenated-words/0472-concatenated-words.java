class Solution {
    public List<String> findAllConcatenatedWordsInADict(String[] words) {
        Set<String> dictionary = new HashSet<>();
        
        //build dictionary
        for (String word : words) {
            dictionary.add(word);
        }
        
        List<String> res = new LinkedList<>();
        for (String word : words) {
            if (isConcatenatedWords(word, dictionary)) {
                res.add(word);
            }
        }
        
        return res;
        
    }
    
    public boolean isConcatenatedWords(String word, Set<String> dictionary) {
        int wordLength = word.length();
        boolean[] dp = new boolean[wordLength];

        for (int cur = 0; cur < wordLength; cur++) {
            if (cur != wordLength - 1) {
                String curString = word.substring(0, cur + 1);
                dp[cur] = dictionary.contains(curString);
                if (dp[cur])
                    continue;
            }
            
            for (int prev = 0; prev < cur; prev++) {
               String cutString = word.substring(prev + 1, cur + 1);
                dp[cur] = dp[cur] || (dp[prev] && dictionary.contains(cutString));
                if (dp[cur])
                    continue;
            } 
        }
        
        
        return dp[wordLength - 1];
    }
}