class Solution {
    public boolean isPalindrome(int x) {
        if (x < 0 || (x != 0 && x%10 == 0)) return false;
        //extract the last half
        int reverse = 0;
        while(x > reverse){
            reverse = reverse*10 + x%10;
            x = x/10;
        }
       // System.out.printf("%d%d",reverse);
        return reverse == x || x == reverse/10;
    }
}