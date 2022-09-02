class Solution {

    public List<String> generateParenthesis(int n) {
        List<String> res = new LinkedList<>();
        this.generate(n, 0, new StringBuilder(), res);
        return res;
    }
    public void generate(int n, int rolling, StringBuilder temp, List<String> res){
        if (rolling == 0 && n == 0){
            res.add(temp.toString());
            return;
        }
        if(rolling < 0) return;
        if(n == 0){
            temp.append(')');
            this.generate(n, rolling-1, temp, res);
            temp.deleteCharAt(temp.length() - 1);
        }
        if(n > 0){
            temp.append('(');
            this.generate(n-1, rolling+1, temp, res);
            temp.deleteCharAt(temp.length() - 1);            
            temp.append(')');
            this.generate(n, rolling-1, temp, res);
            temp.deleteCharAt(temp.length() - 1);   
        }
        
        
        
    }
    
    
    
    
}