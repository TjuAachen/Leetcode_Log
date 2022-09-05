class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        //rolling hash
        int wordLen = words[0].length();
        int wordNum = words.length;
        Map<String, Integer> targetHash = new HashMap<>();
        constructTargetMap(words, targetHash);
        List<Integer> res = new LinkedList<>();
        for(int start = 0; start + wordLen * wordNum - 1 < s.length(); start++){
            Map<String, Integer> curHash = new HashMap<>();
            int prev_end = start;
            for(int end = start + wordLen; end <= start + wordLen * wordNum; end += wordLen){
                String curString = s.substring(prev_end, end);
                if (!targetHash.containsKey(curString))break;
                curHash.computeIfAbsent(curString, k -> 0);
                curHash.put(curString, curHash.get(curString) + 1);
                prev_end = end;
            }
            if (compareTwoMap(targetHash, curHash))
                res.add(start);
            
        }
        return res;
            
            
            
            
        
        
        
    }
    public void constructTargetMap(String[] words, Map<String, Integer> targetHash){
        
        for(String word : words){
            targetHash.computeIfAbsent(word, k->0);
            targetHash.put(word, targetHash.get(word) + 1);
        }
        
        
    }
    public boolean compareTwoMap(Map<String, Integer> targetHash, Map<String, Integer> curHash){
        
        for(Map.Entry<String, Integer> entry : targetHash.entrySet()){
            String key = entry.getKey();
            int num = entry.getValue();
            if(curHash.containsKey(key) && num == curHash.get(key))continue;
            return false;
        }
        return true;
    }
}