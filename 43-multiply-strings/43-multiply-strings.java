class Solution {
    public String multiply(String num1, String num2) {
        String res = "0";
        for(int i = num2.length() - 1; i >= 0; i--){
            String curRes = multiplyOneNum(num1, num2.substring(i, i +1), num2.length() - i - 1);
            res = add(curRes, res);
        }
        return res;
    }

    public String add(String num1, String num2){
        if(num1.length() < num2.length()){
            String temp = num1;
            num1 = num2;
            num2 = temp;
        }
        StringBuilder ans = new StringBuilder();
        int carry = 0;
        for(int i = num1.length()-1; i >= 0; i--){
            int num2Val = 0;
            if(i-num1.length() + num2.length() >= 0){
                int k = i-num1.length() + num2.length();
            num2Val = Integer.valueOf(num2.substring(k, k+1));
            }
            int num1Val = Integer.valueOf(num1.substring(i,i+1));
            int sumRes = num1Val + num2Val + carry;
            String digit = Integer.toString(sumRes%10);
            ans.insert(0, digit);
            carry = sumRes/10;  
        }
        if(carry > 0)ans.insert(0, Integer.toString(carry));
        return ans.toString();
    }
    public String multiplyOneNum(String num1, String num2, int zeroNum){
        StringBuilder tempStr = new StringBuilder();
        String zero = "";
        for(int m = 0; m < zeroNum; m++){
            zero += "0";
        }
        tempStr.append(zero);
        int carry = 0;
        int multiplier = Integer.valueOf(num2.toString());
        for(int i = num1.length() - 1; i >= 0; i--){
            char curNum = num1.charAt(i);
            int num = Character.getNumericValue(curNum);
            int tempRes = num * multiplier + carry;
            tempStr.insert(0, Integer.toString(tempRes%10));
            carry = tempRes/10;
        }
        if(carry > 0){
            tempStr.insert(0, Integer.toString(carry));
        }
        if (tempStr.substring(0,1).equals("0")) return "0";
        return tempStr.toString();  
    }
}