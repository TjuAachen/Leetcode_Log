class Solution {
    public List<Integer> grayCode(int n) {
        //recursion
        //iteration
        return generate(n);
        
        
    }
    public ArrayList<Integer> generate(int n){
        if (n == 1){
            return new ArrayList<Integer>(Arrays.asList(0,1));
        }
        ArrayList<Integer> prev = generate(n - 1);
        int mask = 1<<(n-1);
        for(int i = prev.size() - 1; i >= 0; i--){
            int e = prev.get(i);
            prev.add(e|mask);
        }
        return prev;
    }
    
    
}