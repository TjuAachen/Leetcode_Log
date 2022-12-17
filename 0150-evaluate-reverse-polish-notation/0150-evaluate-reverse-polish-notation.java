class Solution {
    public int evalRPN(String[] tokens) {
        int ans = 0;
        int n = tokens.length;
        LinkedList<Integer> stack = new LinkedList<>();
        
        
        for (String token : tokens){

            if (token.equals("+")){
                int left = stack.pollLast();
                int right = stack.pollLast();
                stack.addLast(left + right);
            }else if (token.equals("-")){
                int left = stack.pollLast();
                int right = stack.pollLast();
                stack.addLast(right - left);     
            }else if (token.equals("*")){
                int left = stack.pollLast();
                int right = stack.pollLast();
                stack.addLast(left * right);
            }else if (token.equals("/")){
                int left = stack.pollLast();
                int right = stack.pollLast();
                stack.addLast( right/left);   
            }else{
                stack.addLast(Integer.parseInt(token));
            }
        }
        
        return stack.pollLast();
    }
}