class Solution {
    private Set<String> hash = new HashSet<>();
    public List<String> removeInvalidParentheses(String s) {
        //find the least number of left, right needed
        int left = 0, right = 0;
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            if(curChar == '('){
                left++;
            }else if(curChar == ')'){
                right++;
                if(left > 0){
                    left--;
                    right--;
                }
            }
        }
        List<String> res = new LinkedList<>();
        remove(0, left, right, 0, s, new StringBuilder(), res);
        return res;
        
        
        
        
        
    }
    public void remove(int start, int left, int right, int rolling, String s, StringBuilder temp, List<String> res){
        if(left < 0 || right < 0||rolling < 0)return;
        if(s.length() == start){
        if(left == 0 && right == 0 && rolling == 0){
            if (!hash.contains(temp.toString())){
                res.add(temp.toString());
                hash.add(temp.toString());
            }
        }
            return;
        }
        char curChar = s.charAt(start);
        int len = temp.length();
        if(curChar == '('){
            //remove (
            this.remove(start + 1, left - 1, right, rolling, s, temp, res);
            //not remove (
            this.remove(start + 1, left, right, rolling + 1, s, temp.append(curChar), res);
            
        }else if(curChar == ')'){
            //remove )
            this.remove(start + 1, left, right - 1, rolling, s, temp, res);
            //not remove )
            this.remove(start + 1, left, right, rolling - 1, s, temp.append(curChar), res);            
        }else{
            this.remove(start + 1, left, right, rolling, s, temp.append(curChar), res);
        }
        temp.setLength(len);
        
    }
}