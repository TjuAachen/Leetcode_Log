class Solution {
    public boolean isNumber(String s) {
        //find the e or E to extract the number
        int i = 0;
        int sLen = s.length();
        while(i < sLen){
            char curChar = s.charAt(i);
            if(curChar == 'e' || curChar == 'E')break;
            i++;
        }
        //no e or E
        String decimal = s.substring(0, i);
        if(i == sLen)return isDecimal(decimal);
        String integer = s.substring(i+1);
        return isDecimal(decimal) && isInteger(integer);
        
    }
    
    public boolean isDecimal(String s){
        //extract two parts integers
        int sLen = s.length();
        if(sLen == 0)return false;
        
        //exclude the first sign digit
        int i = 0;
        int start = 0;
        //exclude the first sign digit
        if(s.charAt(0) == '+' || s.charAt(0) == '-'){
            i += 1;
            start+=1;
        }
        while(i < sLen){
            char curChar = s.charAt(i);
            if(curChar == '.')break;
            i++;
        }
        String secondInteger = "";
        String firstInteger = s.substring(start, i);
        //have '.'
        if(i != sLen)secondInteger = s.substring(i+1);
        boolean res = true;
        if(firstInteger.length() != 0){
            if(firstInteger.charAt(0) == '+' || firstInteger.charAt(0) == '-')return false;
            res &= isInteger(firstInteger);
        }
        if(secondInteger.length() != 0){
            if(secondInteger.charAt(0) == '+' || secondInteger.charAt(0) == '-')return false;
            res &= isInteger(secondInteger);
        }
        if(firstInteger.length() == 0 && secondInteger.length() == 0)return false;
        return res;
    }
    
    
    
    
    public boolean isInteger(String s){
        int sLen = s.length();
        boolean isSign = false;
        
        if (sLen == 0)return false;
        
        if(sLen == 1 && (s.charAt(0) == '+' || s.charAt(0) == '-'))return false;
        int i = 0;
        
        //exclude the first sign digit
        if(s.charAt(0) == '+' || s.charAt(0) == '-'){
            i += 1;
        }
        
        //check if all characters are digits
        while(i < sLen){
            char curChar = s.charAt(i);
            if(!(curChar <= '9' && curChar >= '0'))return false;
            i++;
        }
        return true;
    }
    
    
}