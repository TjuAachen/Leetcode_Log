class Solution {
    private LinkedList<Integer> temp = new LinkedList<>();
    private List<List<Integer>> res = new LinkedList<>();
    private int start = 1;
    public List<List<Integer>> combine(int n, int k) {
        if( k == 0){
            res.add((List) temp.clone());
            return res;
        }
        
        for(int i = start; i < n + 1; i++){
            temp.addLast(i);
            start = i + 1;
            combine(n, k - 1);
            temp.pollLast();
        }
        return res;
    }
}