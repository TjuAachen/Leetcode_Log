class Solution {
    
    public int numDecodings(String s) {
        //@input: string
        //@output : number of ways to decode
        //@edge case : leading 0 
        //@breaking down problem:
        // 1. set the recursion funciton with String s, curRes as input, the final res as output. 
        // 2. in each recursion step, select the first or the first two numbers as the current choice.
        // 3. then the total number of ways is equal to the sum of returned values from the two sub-functions 
        // 4. return the total number of ways as the final result
        //5. when the string is empty, terminate the recursion
        int n = s.length();
        int oneBack = 1, twoBack = 0;
        int temp = 0;
        for(int i = 1; i < n + 1; i++){
            int firstNum = Integer.parseInt(s.substring(i-1, i));
            temp = 0;
            if(firstNum != 0){
                temp += oneBack;
            }
            if (i > 1){
                int secondNum = Integer.parseInt(s.substring(i-2, i - 1));
                int totalNum = secondNum * 10 + firstNum;
                if(totalNum <= 26 && secondNum > 0){
                    temp += twoBack;
                }
            }
            twoBack = oneBack;
            oneBack = temp;
            
            
            
        }
        return temp;
    }
    


    
}