class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        if(tokens.length == 0)return 0;
        
        Arrays.sort(tokens);
        
        int maxPower = power;
        int maxScore = 0;
        int left = 0, right = tokens.length - 1;
        while(left <= right){
            int start = left, end = right;
            int curPower = maxPower;
            int curScore = 0;
            while(start <= end && curPower >= tokens[start]){
                curPower -= tokens[start++];
                curScore++;
            }
            maxScore = Math.max(maxScore, curScore);  
            if(maxPower >= tokens[left]){
            maxPower += tokens[right--] - tokens[left++];
            }else{
                break;
            }
        }
        return maxScore;
    }
}