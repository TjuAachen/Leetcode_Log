class LFUCache {
    Map<Integer, Integer> keyToFreq;
    Map<Integer, Integer> keyToValue;
    Map<Integer, LinkedHashSet> freqToKeys;
    int capacity;
    int minFreq;
    
    public void increaseFreqAndUpdateKey(int key) {
        //get the curFreq
        int curFreq = keyToFreq.get(key);
        //update keyToFreq
        keyToFreq.put(key, curFreq + 1);
        //update freqToKeys
        freqToKeys.get(curFreq).remove(key);
        freqToKeys.putIfAbsent(curFreq + 1, new LinkedHashSet());
        freqToKeys.get(curFreq + 1).add(key);
        
        //update minFreq and freqToKeys
        if (freqToKeys.get(curFreq).isEmpty()) {
            freqToKeys.remove(curFreq);
            if (curFreq == minFreq) {
                minFreq = curFreq + 1;
            }
        }
        
    }
    
    public void removeLFU() {
        if (capacity == 0)
            return;
        //update freqToKeys
        LinkedHashSet<Integer> keyList = freqToKeys.get(minFreq);
        Iterator<Integer> iter = keyList.iterator();
        int removedKey = iter.next();
        keyList.remove(removedKey);
        if (keyList.isEmpty()) 
            keyList.remove(minFreq);
        //update keyToFreq
        keyToFreq.remove(removedKey);
        //update keyToValue
        keyToValue.remove(removedKey);
    }
    
    
    public LFUCache(int capacity) {
        this.capacity = capacity;
        keyToFreq = new HashMap<>();
        keyToValue = new HashMap<>();
        freqToKeys = new HashMap<>();
        minFreq = 0;
    }
    
    public int get(int key) {
        //key exists
        if (keyToFreq.containsKey(key)) {
            increaseFreqAndUpdateKey(key);
            return keyToValue.get(key);
        }
        
        //key not exists
        return -1;
    }
    
    public void put(int key, int value) {
        if (capacity == 0)
            return;
        //k exists
        if (keyToFreq.containsKey(key)) {
            //update key value
            keyToValue.put(key, value);
            //update key freq, and key, minFreq
            increaseFreqAndUpdateKey(key);
            return;
        } 
        // not exists
        if (keyToFreq.size() == capacity) {
            //remove minFreq key
            removeLFU();
        }
        //add new key value
        keyToValue.put(key, value);
        //add key freq
        keyToFreq.put(key, 1);
        //add freq-keys
        freqToKeys.putIfAbsent(1, new LinkedHashSet());
        freqToKeys.get(1).add(key);
        minFreq = 1;
        
       // increaseFreqAndUpdateKey(key);
        
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */