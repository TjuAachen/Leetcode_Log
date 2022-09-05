class Solution {
    public int longestValidParentheses(String s) {
        LinkedList<Integer> potentialStart = new LinkedList<>();
        int ans = 0;
        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);
            if(curChar == '('){
                potentialStart.addLast(i);
            }else if(potentialStart.isEmpty()){
                    potentialStart.addLast(i);    
            }
            else{
                    int idx = potentialStart.pollLast();
                    if(s.charAt(idx) == '('){
                        if(potentialStart.isEmpty()){
                        ans = Math.max(ans, i + 1);
                        }else{
                        ans = Math.max(ans, i - potentialStart.get(potentialStart.size() - 1));
                        }
                    }else{
                        potentialStart.addLast(i);
                    }
                }
            }
    return ans;    
    }

}