class Solution {
    public int[] plusOne(int[] digits) {
        int carry = 1;
        int[] res = new int[digits.length + 1];
        for(int i = digits.length - 1; i >= 0; i--){
            int curRes = digits[i] + carry;
            res[i + 1] = curRes%10;
            carry = curRes/10;
        }
        if(carry > 0){
            res[0] = carry;
            return res;
        }
        return Arrays.copyOfRange(res, 1, digits.length + 1);
    }
}