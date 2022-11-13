class Solution {
    public String reverseWords(String s) {
        
        StringBuilder res = new StringBuilder();
        int cur = 0;
        int totalLen = s.length();
        
        
        while(cur < totalLen){
            char curChar = s.charAt(cur);
            StringBuilder temp = new StringBuilder();
            
            while(cur < totalLen && s.charAt(cur) != ' '){
                curChar = s.charAt(cur);
                temp.append(curChar);
                cur++;
            }
            
            if(!res.isEmpty() && !temp.isEmpty()){
                res.append(' ');
            }
            
            if(curChar == ' '){
                cur++;
            }
            
            res.append(temp.reverse().toString());
            
            
        }
        
        return res.reverse().toString();
        

    }
}