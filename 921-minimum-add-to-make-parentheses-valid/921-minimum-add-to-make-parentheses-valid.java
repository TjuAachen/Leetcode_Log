class Solution {
    public int minAddToMakeValid(String s) {
        int left = 0, right = 0;
        for(int i = 0; i < s.length(); i++){
            char cur_char = s.charAt(i);
            if(cur_char == '('){
                left++;
                
                
            }else if(cur_char == ')'){
                 right++;
                if(left > 0){
                    right--;
                    left--;
                }
            }

        }
        
        return left + right;
    }
}