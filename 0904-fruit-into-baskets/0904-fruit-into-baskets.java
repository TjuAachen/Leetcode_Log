class Solution {
    public int totalFruit(int[] fruits) {
        //two pointers
        int n = fruits.length;
        
        if (n <= 2)
            return n;
        Map<Integer, Integer> counter = new HashMap<>();
        int j = 1;
        int ans = 2;
        counter.put(fruits[0], counter.getOrDefault(fruits[0],0) + 1);
        for (int i = 0; i < n; i++) {
            int curFruit = fruits[i];
       //     counter.computeIfAbsent(curFruit, k -> 0);
            
            j = Math.max(j, i + 1);
            while (j < n && (counter.containsKey(fruits[j]) || counter.size() < 2)) {
              //  System.out.printf("%d %d %b %d\n", i, j, counter.containsKey(fruits[j]), counter.size());
                counter.put(fruits[j], counter.getOrDefault(fruits[j], 0) + 1);
                j++;
            }
            
            ans = Math.max(ans, j - i);
            counter.put(curFruit, counter.get(curFruit) - 1);
            if (counter.get(curFruit) == 0) {
                counter.remove(curFruit);
            }
            if (j == n)
                break;
        }
        
        return ans;
    }
}