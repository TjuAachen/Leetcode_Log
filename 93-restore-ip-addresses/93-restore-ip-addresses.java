class Solution {
    StringBuilder temp = new StringBuilder();
    List<String> res = new LinkedList<>();
    int n = 0;
    public List<String> restoreIpAddresses(String s) {
        if(n == 4 && s.length() == 0){
            res.add(temp.toString());
            return res;
        }
        if(n>0)temp.append(".");
        for(int i = 0; i < Math.min(s.length(),3); i++){
            String cur = s.substring(0,i+1);
            if(cur.charAt(0) == '0' && cur.length() > 1)continue;
        //    System.out.println(cur);
            int curVal = Integer.parseInt(cur);
            if(curVal > 255)break;
            n += 1;
            temp.append(cur);
            restoreIpAddresses(s.substring(i+1));
            n -= 1;
            temp.setLength(temp.length() - i-1);
        }
        if(n > 0)temp.setLength(temp.length() - 1);
        return res;
        
    }
}