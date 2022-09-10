class Solution {
    public String getPermutation(int n, int k) {
        StringBuilder res = new StringBuilder();
        int num = n;
        Set<Integer> visited = new HashSet<>();
        while(num > 0){
        int curDigit = 0;
        while((curDigit + 1)*factorial(num-1) < k){
            curDigit+=1;
        }
        int count = 0;
        for(int i = 1; i < n + 1; i++){
            if(visited.contains(i))continue;
            if(curDigit == count){
                res.append(String.valueOf(i));
                visited.add(i);
            }
            count++;
        }
        k = k - curDigit*factorial(num-1);
        num--;
        }
        return res.toString();
    }
    public int factorial(int n){
        int ans  = 1;
        while(n > 0){
            ans *= n;
            n = n -1;
        }
        return ans;
        
        
        
    }

}