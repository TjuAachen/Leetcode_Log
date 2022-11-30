class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        
        Map<Integer, Integer> counter = new HashMap<>();
        
        for(int elem : arr){
            
            counter.computeIfAbsent(elem, k -> 0);
            counter.put(elem, counter.get(elem) + 1);
        }
        
        
        //occurrence
        Set<Integer> freqSet = new HashSet<Integer>();
        
        for(Map.Entry<Integer, Integer> entry : counter.entrySet()){
            freqSet.add(entry.getValue());
        }
        return freqSet.size() == counter.size();
        
        
    }
}