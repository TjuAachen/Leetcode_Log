class LRUCache {
    Map<Integer, Integer> keyToValues;
    LinkedHashSet<Integer> keyList;
    int capacity;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        keyToValues = new HashMap<>();
        keyList = new LinkedHashSet<>();
    }
    public void updateKey(int key) {
        keyList.remove(key);
        keyList.add(key);
    }
    public int get(int key) {
        //key exists
        if (keyToValues.containsKey(key)) {
            //update keyList
            updateKey(key);
            return keyToValues.get(key);
        }
        
        return -1;
        //not exists
    }
    
    public void removeLRU() {
        //update keyList
        Iterator<Integer> iter = keyList.iterator();
        int removedKey = iter.next();
        keyList.remove(removedKey);
        //update keyValue
        keyToValues.remove(removedKey);
    }
    
    public void put(int key, int value) {
        //key exists
        if (keyToValues.containsKey(key)) {
            keyToValues.put(key, value);
            //update keyList
            updateKey(key);
            return;
        }
        //not exists
        if (keyList.size() == capacity) {
            //remove LRU key
            removeLRU();
        }
        //not exist
        keyToValues.put(key, value);
        keyList.add(key);
        
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */