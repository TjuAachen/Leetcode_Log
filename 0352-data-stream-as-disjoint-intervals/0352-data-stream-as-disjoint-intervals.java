class SummaryRanges {
    
    TreeMap<Integer, Integer> tree_map;
    
    public SummaryRanges() {
        tree_map = new TreeMap<>();
    }
    
    public void addNum(int value) {
        Integer floorKey = tree_map.floorKey(value);
        Integer ceilingKey = tree_map.ceilingKey(value);
        int left = value;
        int right = value;
        //merge left
        if (floorKey != null) {
            if (tree_map.get(floorKey) >= value)
                return;
            if (tree_map.get(floorKey) == value - 1)
                left = floorKey;
        }
        if (ceilingKey != null && ceilingKey == value + 1) {
            right = tree_map.get(ceilingKey);
            tree_map.remove(ceilingKey);
        }
        
        tree_map.put(left, right);
        
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