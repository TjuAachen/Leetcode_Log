class Solution {
    public String minRemoveToMakeValid(String s) {
        LinkedList<Integer> stack = new LinkedList<>();
        Set<Integer> idxToRemove = new HashSet<>();
        for(int i = 0; i < s.length(); i++){
            char cur_char = s.charAt(i);
            if(cur_char == '('){
                stack.add(i);
                idxToRemove.add(i);
            }else if(cur_char == ')'){
                if(!stack.isEmpty()){
                    idxToRemove.remove(stack.poll());
                }else{
                    idxToRemove.add(i);
                }
                
            }
        }
        StringBuilder res = new StringBuilder();
        for(int j = 0; j < s.length(); j++){
            if(!idxToRemove.contains(j))res.append(s.charAt(j));
        }
        return res.toString();
        
    }
}