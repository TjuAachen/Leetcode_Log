class Solution {
    public int[] findOriginalArray(int[] changed) {
        Arrays.sort(changed);
        int K = changed.length;
        HashMap<Integer, Integer> needNum = new HashMap<>();

        int[] ans = new int[K/2];
        int k = 0;
        if(K%2 != 0)return new int[]{};
        for(int i = 0; i < K; i++){
            int curNum = changed[i];
            if(needNum.containsKey(curNum)){
                needNum.put(curNum, needNum.get(curNum) - 1);
                if(needNum.get(curNum) == 0)needNum.remove(curNum);
                continue;
            }else{
                if(k >= K/2)return new int[]{};
                ans[k++] = curNum;
                needNum.computeIfAbsent(2*curNum, m -> 0);
                needNum.put(2*curNum, needNum.get(2*curNum) + 1);
            }
            
        }
        if(needNum.size() == 0)return ans;
        return new int[]{};
        
        
    }
}