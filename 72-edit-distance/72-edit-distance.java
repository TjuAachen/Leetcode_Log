class Solution {
    Map<String, Integer> memo = new HashMap<>();
    int MAX = 20000;
    public int minDistance(String word1, String word2) {
        int startLen = word1.length();
        int targetLen = word2.length();
        String key = word1+"#" + word2;
        
        if(memo.containsKey(key)){
            return memo.get(key);
        }
        
        if(startLen == 0){
            if(targetLen == 0)return 0;
            return targetLen;
        }
        
        if(targetLen == 0)return startLen - targetLen;
        int ans = MAX;
        //three possible cases
        char startFirst = word1.charAt(0), targetFirst = word2.charAt(0);
        if(startFirst == targetFirst){
            ans = Math.min(minDistance(word1.substring(1), word2.substring(1)), ans);
        }else{
            //replace
            ans = Math.min(minDistance(word1.substring(1), word2.substring(1)) + 1, ans);
            
            //delete
            ans = Math.min(minDistance(word1.substring(1), word2) + 1, ans);
            //insert
            ans = Math.min(minDistance(word1, word2.substring(1)) + 1, ans);                  
        }
        memo.put(key, ans);
        return ans;        
    }
}