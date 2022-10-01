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
        return numCurDecodings(s, new HashMap<String, Integer>());
    }
    
    public int numCurDecodings(String s, Map<String, Integer> memo){
        if(s.length() == 0){
            return 1;
        }
        if(memo.containsKey(s))return memo.get(s);
        int curRes = 0;
        int firstNum = Integer.parseInt(s.substring(0,1));
        if (firstNum != 0){
            curRes += numCurDecodings(s.substring(1), memo);
        }
        if (firstNum <= 2 && firstNum > 0 && s.length() > 1){
            int secondNum = Integer.parseInt(s.substring(1,2));
            int firstTwoNum = firstNum * 10 + secondNum;
            
            if(firstTwoNum <= 26)curRes += numCurDecodings(s.substring(2), memo);
        }
        memo.put(s, curRes);
        return curRes;
        
        
        
    }

    
}