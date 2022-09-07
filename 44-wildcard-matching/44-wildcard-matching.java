class Solution {
    HashMap<String, Boolean> memo = new HashMap<>();
    public boolean isMatch(String s, String p){
        int num = count(p);
        return this.isMatchRes(s, p, num);
        
    }
    public boolean isMatchRes(String s, String p, int num) {
        String key = s + "#" + p;
        if(memo.containsKey(key))return memo.get(key);
        if(s.length() == 0 && p.length() == 0)return true;
        if(s.length() == 0){
            for(int i = 0; i < p.length(); i++){
                if(p.charAt(i) != '*'){
                    memo.put(key, false);
                    return false;}
            }
            memo.put(key, true);
            return true;
        }
        if(s.length() == 0 || p.length() == 0)return false;
        String sNxt = s.substring(1), pNxt = p.substring(1);
        boolean tempRes = false;
        if(p.charAt(0) == s.charAt(0)){
            if(num - 1 <= sNxt.length()){
            tempRes |= isMatchRes(sNxt, pNxt, num - 1);}
            memo.put(key, tempRes);
            return tempRes;
        }else if(p.charAt(0) == '*'){
            if(num <= sNxt.length()){
            tempRes |= isMatchRes(sNxt, p, num);
            tempRes |= isMatchRes(sNxt, pNxt, num);
                
            }
            if(num <= s.length()){
                tempRes |= isMatchRes(s, pNxt, num);}
            memo.put(key, tempRes);
            return tempRes;
        }else if(p.charAt(0) == '?'){
            if(num - 1 <= sNxt.length()){
            tempRes |= isMatchRes(sNxt, pNxt, num - 1);}
            memo.put(key, tempRes);
            return tempRes;
        }
        return tempRes;
        
    }
    public int count(String p){
        int res = 0;
        for(int i = 0; i < p.length(); i++){
            if(p.charAt(i) != '*')res++;
        }
        return res;
        
        
    }
}