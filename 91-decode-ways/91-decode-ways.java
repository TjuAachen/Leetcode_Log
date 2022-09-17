class Solution {
    Map<Integer, Integer> memo = new HashMap<>();
    public int numDecodings(String s) {
        //exclude leading zeros
        if(s.charAt(0) == '0')return 0;
        if(s.length() == 1 && !s.equals("0"))return 1;
        //no leading zeros
        return findNum(s, 0);
        
    }
    
    public int findNum(String s, int start){
        if(memo.containsKey(start))return memo.get(start);
        if(start == s.length())return 1;
        if(start == s.length() - 1){
            if(s.charAt(start) == '0')return 0;
            return 1;
        }
        int ans = 0;
        //take 1
        if(s.charAt(start) == '0')return 0;
        ans += findNum(s, start + 1);
        //take 2
        String twoNum = s.substring(start, start + 2);
        int num = Integer.parseInt(twoNum);
        //exclude the leading zero
        if(num <= 26 && num >= 1){
            ans += findNum(s, start + 2);
        }
        memo.put(start, ans);
        return ans;
        
        
    }
    
    
}