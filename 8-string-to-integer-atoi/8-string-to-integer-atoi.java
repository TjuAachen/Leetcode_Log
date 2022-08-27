class Solution {
    public int myAtoi(String s) {
        //remove leading whitespace
        s = s.replaceAll("^\\s+","");
        // the first digit
        if (s.length() == 0)
            return 0;
        
        int sign = 1;
        if (s.charAt(0) == '-')
            sign = -1;
        int res = 0;
        
        
        if (Character.isDigit(s.charAt(0))){
            res = Character.getNumericValue(s.charAt(0));
        }
        
        if(!Character.isDigit(s.charAt(0)) && s.charAt(0) != '-' && s.charAt(0) != '+')
            return 0;
        
        int pointer = 0;
        //read digit till non-digit

        s = s.substring(1);
        res = sign * res;
        while(pointer < s.length() && Character.isDigit(s.charAt(pointer))){
            int cur_num = Character.getNumericValue(s.charAt(pointer++));
            //negative overflow
            if (sign == -1){
            // not negative overflow
            if (res < Integer.MIN_VALUE/10 || (res == Integer.MIN_VALUE / 10 && cur_num > 8))
                return Integer.MIN_VALUE;
            res = 10 * res - cur_num;
            }
            else{
            
                if (res > Integer.MAX_VALUE/10 || (res == Integer.MAX_VALUE / 10 && cur_num > 7))
                return Integer.MAX_VALUE;
            res = res * 10 + cur_num;
            
            }
        }
        
        return res;
        
        
    }
}