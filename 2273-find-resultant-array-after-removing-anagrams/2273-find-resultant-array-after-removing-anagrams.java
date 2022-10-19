class Solution {
    public List<String> removeAnagrams(String[] words) {
        LinkedList<String> stack = new LinkedList<>();
        
        for(String word : words){
            if(stack.isEmpty() || !isAnagram(stack.peekLast(), word)){
                stack.add(word);
            }
        }
        return stack;
        
        
    }
    private boolean isAnagram(String s1, String s2){
        int[] ansS1 = countChar(s1);
        int[] ansS2 = countChar(s2);
        for(int i = 0; i < 26; i++){
            if(ansS1[i] != ansS2[i])return false;
        }
        return true;
    }
    
    private int[] countChar(String s){
        int[] ans = new int[26];
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            ans[curChar - 'a'] += 1;
        }
        return ans;
        
        
        
        
    }
}