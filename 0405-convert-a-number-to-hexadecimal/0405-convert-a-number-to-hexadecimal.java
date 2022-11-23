class Solution {
    public String toHex(int num) {
        
        if(num == 0){
            return "0";
        }
        
        long newNum = num;
        if(num < 0){
            newNum = (long) Math.pow(2, 32) + num;
        }

        StringBuilder res = new StringBuilder();
        
        while(newNum > 0){
            
            int order = 0;
            long temp = newNum;
            long curRes = 1;
            while(temp/16 > 0){
                temp /= 16;
                order += 1;
                curRes *= 16;
            }
            
            long curBit =  newNum / curRes;
            
            newNum -= curBit * curRes;
            
            String bit;
            
            if(curBit < 10){
                bit = String.valueOf(curBit);
            }else{
                char tempBit =(char)((int) 'a' + (curBit - 10));
                bit = String.valueOf(tempBit);
            }
            
            if(res.isEmpty()){
                res.append(bit);
                for(int i = 1; i <= order; i++){
                    res.append("0");
                }
            }else{
                res.replace(res.length() - 1 - order, res.length() - order, bit);
            }
            
        }
        
        return res.toString();
    }
    
}