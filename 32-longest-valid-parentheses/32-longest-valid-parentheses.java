class Solution {
    public int longestValidParentheses(String s) {
        //find the leftmost starting point
        LinkedList<Integer> stack = new LinkedList<>();
        int res = 0;
        for(int i = 0; i < s.length(); i++){
            char cur_char = s.charAt(i);
            //new starting point
            if(cur_char == '('){
                stack.add(i);
            }else{
                if (!stack.isEmpty()){
                    int idx = stack.pollLast();
                    if(!stack.isEmpty()){
                        res = Math.max(res, i - stack.peekLast());
                    }else if(s.charAt(idx) == '('){
                        res = Math.max(res, i + 1);
                    }else{
                        stack.offerLast(i);
                    }
                    
                }else{
                    stack.offerLast(i);
                }
                
            }
           // System.out.println(res);
            
            
            
        }
        return res;
        
    }
}