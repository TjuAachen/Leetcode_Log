class Solution {
    private StringBuilder finalRes = null;
    public String countAndSay(int n) {
        StringBuilder ans = new StringBuilder("1");
        res(1, n, ans);
        return finalRes.toString();
    }
    public void res(int n, int m, StringBuilder temp){
        if(n == m){
            finalRes = temp;
            return;
        }
        List<Character> c = new LinkedList<Character>();
        StringBuilder nxt = new StringBuilder();
        for(int i = 0; i < temp.length(); ){
            char curChar = temp.substring(i,i+1).charAt(0);
            int curCount = 0;
            while(i < temp.length() && curChar == temp.substring(i,i+1).charAt(0)){
                curCount += 1;
                i++;
            }
            nxt.append(Integer.toString(curCount));
            nxt.append(curChar);
            
        }
        temp = nxt;
        
        res(n + 1, m, temp);
    }
    
    
}