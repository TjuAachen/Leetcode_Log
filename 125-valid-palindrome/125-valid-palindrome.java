class Solution {
    public boolean isPalindrome(String s) {
        //input : string upper -> lowercase, remove all non-alphanumeric
        //output : boolean, if it is a palindrome
        //breaking down:
        //1.preprocess
        //2.verify it is palindrome
        String processedS = RemoveNonLetterConvertLower(s);
        return verify(processedS);
        
        
    }
    public String RemoveNonLetterConvertLower(String s){
        StringBuilder res = new StringBuilder();
        s = s.toLowerCase();
        for (int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            if(Character.isLetterOrDigit(curChar)){
                res.append(String.valueOf(curChar));
            }
        }
        return res.toString();
    }
    public boolean verify(String s){
        int n = s.length();
        for(int i = 0; i < n/2; i++){
            int idx = n - 1 - i;
            if(s.charAt(i) != s.charAt(idx))return false;
        }
        return true;
    }
    
    
}