class Solution {
    Set<String> words = new HashSet<>();
    public List<String> wordBreak(String s, List<String> wordDict) {
        for(String word : wordDict){
            words.add(word);
        }
        List<String> res = new LinkedList<>();
        findSentences(s, 0, new StringBuilder(), res);
        return res;
        
        
    }
    public void findSentences(String s, int start, StringBuilder temp, List<String> res){
        if(s.length() == start){
            res.add(temp.toString());
            return;
        }
        for(int i = start + 1; i < s.length() + 1; i++){
            String selectedString = s.substring(start, i);
            if(!words.contains(selectedString))continue;
            int extra = 0;
            if (start != 0){
                temp.append(" ");
                extra = 1;
            }
            temp.append(selectedString);
            findSentences(s, i, temp, res);
            temp.setLength(temp.length() - selectedString.length() - extra);
        }
        
        
        
        
        
        
    }
}