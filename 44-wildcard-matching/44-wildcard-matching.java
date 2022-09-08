class Solution {

    public boolean isMatch(String s, String p){
        int pIdx = 0, sIdx = 0;
        int starIdx = -1, sTmpIdx = -1;
        int sLen = s.length(), pLen = p.length();
        while(sIdx < sLen){
            if(pIdx == pLen){
                if(starIdx == -1)return false;
                pIdx = starIdx + 1;
                sIdx = sTmpIdx + 1;
                sTmpIdx = sIdx;
            }else if(p.charAt(pIdx) == s.charAt(sIdx) || p.charAt(pIdx) == '?'){
                pIdx++;
                sIdx++;
            }else if(p.charAt(pIdx) == '*'){
                starIdx = pIdx;
                sTmpIdx = sIdx;
                pIdx ++;
                
                
            }else if(starIdx == -1){
                return false;
            }else{
                pIdx = starIdx + 1;
                sIdx = sTmpIdx + 1;
                sTmpIdx = sIdx;
            
            } 
            
        }
        for (int i = pIdx; i < pLen; i++) {
            if (p.charAt(i) != '*') {
                return false;
            }
   
        }
        return true;
        
        
    }



}