class Solution {
    private String res;
    private Set<Integer> visited = new HashSet<>();
    private int N;
    private int curNum = 1;
    public String getPermutation(int n, int k) {
        N = n + 1;
        permutation(n, new StringBuilder(), k);
        return res;
    }
    public boolean permutation(int n, StringBuilder temp, int k){

        if(n == 0){
            if(curNum == k){
                res = temp.toString();
                return true;
            }
            curNum++;
            return false;
        }
        for(int i = 1; i < N; i++){

            if(visited.contains(i))continue;
            
            visited.add(i);
            String m = String.valueOf(i);
            temp.append(m);
            if (permutation(n - 1, temp, k)) return true;
            temp.setLength(temp.length() -1);
            visited.remove(i);
        }
        return false;
    }
}