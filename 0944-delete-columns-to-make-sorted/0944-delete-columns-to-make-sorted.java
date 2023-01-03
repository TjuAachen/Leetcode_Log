class Solution {
    public int minDeletionSize(String[] strs) {
        int answer = 0;
        int nCol = strs[0].length();
        
        for (int col = 0; col < nCol; col++){
            for (int row = 1; row < strs.length; row++){
                if (strs[row].charAt(col) < strs[row - 1].charAt(col)){
                    answer++;
                    break;
                }
            }
        }
        
        return answer;
            

    }
}