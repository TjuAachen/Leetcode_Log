class Solution {
    public int longestValidParentheses(String s) {
        int rollingLeft = 0, rollingRight = 0;
        int ans = 0;
        //left-pass
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            if(curChar == '('){
                rollingLeft += 1;
            
            }else{
                rollingRight += 1;
            }
            if(rollingLeft == rollingRight){
                ans = Math.max(ans, rollingRight * 2);
                
            }else if(rollingLeft < rollingRight){
                rollingLeft = rollingRight = 0;
            }
        }
        rollingLeft = 0;
        rollingRight = 0;
        for(int i = s.length() - 1; i >= 0; i--){
            char curChar = s.charAt(i);
            if(curChar == '('){
                rollingLeft += 1;
            
            }else{
                rollingRight += 1;
            }
            if(rollingLeft == rollingRight){
                ans = Math.max(ans, 2 * rollingRight);
                
            }else if(rollingLeft > rollingRight){
                rollingLeft = rollingRight = 0;
            }
        }
        return ans;
        
    
    }

}