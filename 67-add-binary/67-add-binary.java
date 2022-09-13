class Solution {
    public String addBinary(String a, String b) {
        StringBuilder res = new StringBuilder();
        int aLen = a.length(), bLen = b.length();
        int i = aLen - 1, j = bLen - 1;
        int carry = 0;
        while(i >= 0 || j >= 0){
            int aChar = 0;
            int bChar = 0;
            if(i >=0){
                aChar = a.charAt(i--) - '0';
            }
             if(j >=0){
                bChar = b.charAt(j--) - '0';
            }
            int curRes = aChar + bChar + carry;
            carry = curRes/2;
            res.append(String.valueOf(curRes%2));
        }
        if(carry == 1){
            res.append("1");
        }
        return res.reverse().toString();
        
    }
}