class Solution {
    public boolean validWordAbbreviation(String word, String abbr) {
        
        StringBuilder unAbbr = new StringBuilder();
        
        int i = 0;
        int size = abbr.length();
        int temp = 0;
        while(i < size){
            char curChar = abbr.charAt(i);
            if(curChar == '0'){
                if(temp == 0)
                    return false;
                temp *= 10;
            }else if(curChar <= '9' && curChar > '0'){
                temp = temp * 10 + (curChar - '0');
            }else{
                for(int j = 0; j < temp; j++){
                    unAbbr.append("*");
                }
                temp = 0;
                unAbbr.append(String.valueOf(curChar));
            }
            
            i++;
        }
        if(temp > word.length())
            return false;
        for(int j = 0; j < temp; j++){
                    unAbbr.append("*");
        }
        
        int unAbbrSize = unAbbr.length();
        
        if(unAbbrSize != word.length())
            return false;
        
        int k = 0;
        
        while(k < unAbbrSize){
            char abbrChar = unAbbr.charAt(k);
            if(abbrChar != '*' && abbrChar != word.charAt(k))
                return false;
            
            k++;
        }
        
        return true;
        
    }
    
}