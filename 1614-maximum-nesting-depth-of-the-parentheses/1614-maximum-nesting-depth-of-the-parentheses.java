class Solution {
    private int i = 0;
    public int maxDepth(String s) {
        int N = s.length();
        int temp = 0;
        while(i < N){
            char cur_char = s.charAt(i);
            i++;
            if(cur_char == '('){
                temp = Math.max(temp, this.maxDepth(s));
            }else if(cur_char == ')'){
                temp++;
                break;
            }
        }
        return temp;
    }
}