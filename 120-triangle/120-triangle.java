class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        ArrayList<ArrayList<Integer>> res = new ArrayList<>();
        int count = 0;
        int ans = Integer.MAX_VALUE;
        for(List<Integer> temp : triangle){
            ArrayList<Integer> cur = new ArrayList<>();
            
            if(count == 0){
                cur.add(temp.get(0));
                res.add(cur);
            if(count == triangle.size() -1){
                    ans = Math.min(temp.get(0), ans);
                //    System.out.println(Math.min(left, right) + temp.get(i));
                }
                count++;
                continue;
            }
            ArrayList<Integer> prev = res.get(count-1);
            for(int i = 0; i < temp.size(); i++){
                int left = Integer.MAX_VALUE, right = Integer.MAX_VALUE;
                if(i > 0){
                    left = prev.get(i-1);
                }
                if(i < temp.size() - 1)right = prev.get(i);
                cur.add(Math.min(left, right) + temp.get(i));
                if(count == triangle.size() -1){
                    ans = Math.min(Math.min(left, right) + temp.get(i), ans);
                //    System.out.println(Math.min(left, right) + temp.get(i));
                }
            }
            count++;
            res.add(cur);
        }
        return ans;
        
        
        
    }
}