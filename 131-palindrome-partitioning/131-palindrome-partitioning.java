class Solution {
    public List<List<String>> partition(String s) {
        //@input : string s
        //@output: all possible palindrome partitioning of s
        //@edge case : no
        //@breaking down problem:
        // 1. backtracking
        // 2. if come to the end, then terminate
        // 3. in each step, select the palindrome one
        List<List<String>> res = new LinkedList<>();
        List<String> temp = new LinkedList<>();
        backtracking(s, 0, res, temp);
        return res;
        
        
        
    }
    public boolean isPalindrome(String s){
        int n = s.length();
        int i = 0;
        while(i < n / 2){
            if(s.charAt(i) != s.charAt(n - 1 - i))return false;
            i++;
        }
        return true;
    }
    
    public void backtracking(String s, int curPointer, List<List<String>> res, List<String> temp){
        //termination
        
        if(curPointer == s.length()){
            res.add(new LinkedList<>(temp));
            return;
        }
        for(int i = curPointer; i < s.length(); i++){
            //select
            String curPartition = s.substring(curPointer, i + 1);
            if(isPalindrome(curPartition)){
                temp.add(curPartition);
                backtracking(s, i + 1, res, temp);
                temp.remove(temp.size() - 1);
            }
        }
    }
    
    
}