class Solution {
    public int minAddToMakeValid(String s) {
        int rolling = 0;
        LinkedList<Integer> stack = new LinkedList<>();
        for(int i = 0; i < s.length(); i++){
            char cur_char = s.charAt(i);
            if(cur_char == '(')
                stack.add(i);
            if(cur_char == ')')
                if (!stack.isEmpty()){
                    stack.poll();
                }else{
                    rolling++;
                }
        }
        return stack.size() + rolling;
    }
}