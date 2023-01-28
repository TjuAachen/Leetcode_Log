class SummaryRanges {
    
    TreeMap<Integer, Integer> tree_map;
    
    public SummaryRanges() {
        tree_map = new TreeMap<>();
    }
    
    public void addNum(int value) {
        Integer floorKey = tree_map.floorKey(value);
        Integer ceilingKey = tree_map.ceilingKey(value);
        //merge with both sides
        boolean mergeLeft = false;
        boolean mergeRight = false;
        
        if (floorKey != null && tree_map.get(floorKey) + 1 >= value)
            mergeLeft = true;
        if (ceilingKey != null && value + 1 == ceilingKey)
            mergeRight = true;
        
        if (mergeLeft == false && mergeRight == false)
            tree_map.put(value, value);
        if (mergeLeft && !mergeRight) 
            tree_map.put(floorKey, Math.max(tree_map.get(floorKey),value));
        if (mergeRight) {
            if (mergeLeft) {
                tree_map.put(floorKey, tree_map.get(ceilingKey));
            }else {
                tree_map.put(value, tree_map.get(ceilingKey));
            }
            tree_map.remove(ceilingKey);
        }
    }
    
    public int[][] getIntervals() {
        int n = tree_map.size();
        int[][] intervals = new int[n][2];
        int start = 0;
        for (Map.Entry<Integer, Integer> entry : tree_map.entrySet()) {
            intervals[start][0] = entry.getKey();
            intervals[start][1] = entry.getValue();
            start++;
        }
        
        return intervals;
    }
}

/**
 * Your SummaryRanges object will be instantiated and called as such:
 * SummaryRanges obj = new SummaryRanges();
 * obj.addNum(value);
 * int[][] param_2 = obj.getIntervals();
 */