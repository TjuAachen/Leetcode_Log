class Solution {
    public int[] numsSameConsecDiff(int n, int k) {
        //first number enumeration
        LinkedList<Integer> res = new LinkedList<>();
        for(int i = 1; i < 10; i++){
            this.numsDiff(n - 1, k, i, i, res);
        }
        int[] ans = new int[res.size()];
        for(int j = 0; j < res.size(); j++)
            ans[j] = res.get(j);
        return ans;
        
        
    }
    public void numsDiff(int n, int k, int prev, int temp, LinkedList<Integer> res){
        if (n == 0){
            res.addLast(temp);
            return;
        }
        if (prev - k >= 0){
            this.numsDiff(n - 1, k, prev - k, temp * 10 + prev - k , res);
        }
        if (prev + k < 10 && prev-k!= prev+k){
            this.numsDiff(n - 1, k, prev + k, temp * 10 + prev + k , res);
        }
        
        
    }
}