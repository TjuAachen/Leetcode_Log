class RandomizedSet {
    
    private Map<Integer, Integer> randomMap;
    private ArrayList<Integer> randomList;
    private int size;
    Random rand = new Random(); 
    
    public RandomizedSet() {
        randomMap = new HashMap<>();
        randomList = new ArrayList<>();
        size = 0;
    }
    
    public boolean insert(int val) {
        
        if(!randomMap.containsKey(val)){
            randomMap.put(val, size);
            size += 1;
            randomList.add(val);
            
            return true;
        }
        return false;
        
    }
    
    public boolean remove(int val) {
        
        if(!randomMap.containsKey(val))
            return false;
        //exchange and then remove
        int removedIdx = randomMap.get(val);

        randomList.set(removedIdx, randomList.get(size - 1));
        
        randomMap.put(randomList.get(size - 1), removedIdx);
        randomMap.remove(val);
        randomList.remove(size - 1);
        
        
        

        size -= 1;
        
        return true;
        
    }
    
    public int getRandom() {
        
        int selectedIdx = rand.nextInt(size);
        return randomList.get(selectedIdx);
        
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */