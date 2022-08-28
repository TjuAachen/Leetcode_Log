class Solution {
    public int romanToInt(String s) {
        Map<String, Integer> strToVal = new HashMap<>(){{put("I",1);put("V",5);put("X", 10);put("L", 50);put("C", 100); put("D", 500); put("M", 1000); put("IV", 4); put("IX", 9); put("XL", 40); put("XC", 90); put("CD", 400); put("CM", 900);}};
        int N = s.length();    
        int res = 0;
        int i = 0;
        
        while(i < N){
            String cur_char = s.substring(i, i+1);
            if (i+2 <= N && strToVal.containsKey(s.substring(i, i+2))){
                res += strToVal.get(s.substring(i, i+2));
                i += 2;
            }else{
                res += strToVal.get(cur_char);
                i++;
            }
            
        }
        return res;
        
    }
}