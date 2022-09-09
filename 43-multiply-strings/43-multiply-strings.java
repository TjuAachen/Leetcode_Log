class Solution {
    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0")) {
            return "0";
        }
        StringBuilder ans = new StringBuilder();
        StringBuilder firstNumber = new StringBuilder(num1);
        StringBuilder secondNumber = new StringBuilder(num2);
        
        //reverse both the numbers
        firstNumber.reverse();secondNumber.reverse();
        
        for(int i = 0; i < secondNumber.length() + firstNumber.length(); i++){
            ans.append('0');
        }
        
        for(int place2 = 0; place2 < secondNumber.length(); place2++)
            for(int place1 = 0; place1 < firstNumber.length(); place1++){
                int digit1 = firstNumber.charAt(place1) - '0';
                int digit2 = secondNumber.charAt(place2) - '0';
                
                int currentPos = place1 + place2;
                int carry = ans.charAt(currentPos) - '0';
                int multiplication = digit1*digit2 + carry;
                
                ans.setCharAt(currentPos, (char) (multiplication%10 +'0'));
                
                int value = (ans.charAt(currentPos + 1) - '0') + multiplication / 10;
                ans.setCharAt(currentPos + 1, (char)(value + '0'));
                
            }
        //Pop excess 0 from the rear of answer
        if(ans.charAt(ans.length() - 1) == '0'){
            ans.deleteCharAt(ans.length() - 1);
        }
        ans.reverse();
        return ans.toString();
        
        
        
        
        
    }

}