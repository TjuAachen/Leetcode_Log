class Solution {
    int i = 0;
    public int calculate(String s) {
        
        LinkedList<Integer> stack = new LinkedList<>();
        
        
        int res = 0;
        int sign = 1;
        
        int num = 0;
        
        int length = s.length();
        
        while(i < length){
            char curChar = s.charAt(i);
            
            if(curChar <= '9' && curChar >= '0'){
                num = num * 10 + (curChar - '0');
            }else if(curChar == '('){
                i++;
                int temp = sign * calculate(s);
                stack.add(temp);
            }else if(curChar == ')'){
                if(num != 0){
                    stack.add(sign * num);
                    num = 0;
                }
                break;
                
            }else if(curChar == '+'){
                if(num != 0){
                    stack.add(sign * num);
                    num = 0;
                }
                
                sign = 1;
            }else if(curChar == '-'){
                if(num != 0){
                    stack.add(sign * num);
                    num = 0;
                }
                sign = -1;
            }
            
            i++;
        }
        if(i == length && num != 0){
            stack.add(sign * num);
            num = 0;
        }

        for(Integer elem : stack){
            res += elem;
        }
        
        return res;
    }
}