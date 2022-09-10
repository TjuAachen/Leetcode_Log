class Solution {
    public int lengthOfLastWord(String s) {
        StringBuilder res = new StringBuilder(s).reverse();
        int ans = 0;
        boolean hasWord = false;
        for(int i = 0; i < res.length(); i++){
            if(res.charAt(i) == ' ' && hasWord){
                break;
            }else if(res.charAt(i) != ' '){
                ans++;
                hasWord = true;
            }
        }
        return ans;
    }
}