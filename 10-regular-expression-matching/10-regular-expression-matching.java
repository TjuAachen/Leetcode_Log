class Solution {
    public boolean isMatch(String s, String p) {
        if (s.length() != 0 && p.length() == 0) return false;
        if (s.length() == 0 && p.length() == 0) return true;

        boolean res = false;
        if (p.charAt(0) == '.'){
            //is * there?
            if (p.length() > 1 && p.charAt(1) == '*'){
                //take it
                if (s.length() > 0)
                    res = res || this.isMatch(s.substring(1), p);
                //not take it
                res = res || this.isMatch(s, p.substring(2));
                } else if (s.length() > 0){
                    res = res || this.isMatch(s.substring(1), p.substring(1));
                }
            }else if (p.length() > 1 && p.charAt(1) == '*'){
                //take it
                if (s.length() > 0 && p.charAt(0) == s.charAt(0))
                    res = res || this.isMatch(s.substring(1), p);
                //not take it
                res = res || this.isMatch(s, p.substring(2));
        }else if (s.length() > 0 && s.charAt(0) == p.charAt(0)){
                    res = res || this.isMatch(s.substring(1), p.substring(1));
                }        
        return res;  
}
}

        
