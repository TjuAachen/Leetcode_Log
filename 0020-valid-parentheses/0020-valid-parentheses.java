class Solution {
    public boolean isValid(String s) {
        LinkedList<Character> stack = new LinkedList<>();
        int N = s.length();
        HashMap<Character, Character> left_par = new HashMap<>(){{put('(', ')'); put('{','}'); put('[',']');}};
        for(int i = 0; i < N; i++){
            char cur_char = s.charAt(i);
            if(stack.isEmpty() && left_par.containsKey(cur_char)){
                stack.add(cur_char);
            }else if(stack.isEmpty()){
                return false;
            }
            else{
                char last = stack.get(stack.size() - 1);
                if (left_par.containsKey(cur_char)){
                    stack.add(cur_char);
                }else{
                    if(left_par.get(last) != cur_char) return false;
                    stack.pollLast();

                }
            }
            }
        if(stack.isEmpty())return true;
        return false;
    }
        
    }
