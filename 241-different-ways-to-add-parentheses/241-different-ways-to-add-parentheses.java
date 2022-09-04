class Solution {
    public List<Integer> diffWaysToCompute(String expression) {
        //find operator
        int N = expression.length();
        List<Integer> res = new LinkedList<>();
        for(int i = 0; i < N; i++){
            char letter = expression.charAt(i);
            if(letter == '+' || letter == '-' || letter == '*'){
                List<Integer> leftRes = this.diffWaysToCompute(expression.substring(0, i));
                List<Integer> rightRes = this.diffWaysToCompute(expression.substring(i+1));
                //combine
                for(int left : leftRes)
                    for(int right : rightRes){
                        if(letter == '+'){
                            res.add(left + right);
                        }else if(letter == '-'){
                            res.add(left - right);
                        }else if(letter == '*'){
                            res.add(left*right);
                        }
                        
                        
                    }
                
                
            }
        }
        //pure integer
        if(res.size() == 0){
            res.add(Integer.parseInt(expression));
        }
        return res;
        
    }

}