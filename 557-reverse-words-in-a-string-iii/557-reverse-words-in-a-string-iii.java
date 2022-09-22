class Solution {
    public String reverseWords(String s) {
        //@input String s "Let's take leetcode contest"
        
        //@output
        
        //1.tokenize each vocabulary by the interval
        int idx = 0;
        StringBuilder res = new StringBuilder();
        while(idx < s.length()){
            char curChar = s.charAt(idx);
            String token = extractWord(s, idx);
            String reversedToken = reverseWord(token);
            res.append(reversedToken);
            res.append(" ");
            idx += token.length() + 1;
            
        }
        res.setLength(res.length() - 1);
        return res.toString();
        
        //2.then reverse each token one by one
        //3.add the reversed token into the final result
        
        
        
        //@edge case, when the word is empty/leading or trailing spaces
        //no word would contain intervals.
        //the num of intervals between two neighboring words is exactly 1.    
    }
    //string is transferred, then the first token is output
    public String extractWord(String s, int start){
        StringBuilder temp = new StringBuilder();
        while(start < s.length() && s.charAt(start) != ' '){
            temp.append(s.charAt(start));
            start++;
        }
        return temp.toString();
    }
    
    
    
    //one token is input, then the reversed word is output
    public String reverseWord(String word){
        StringBuilder temp = new StringBuilder(word).reverse();
        return temp.toString();
    }
}