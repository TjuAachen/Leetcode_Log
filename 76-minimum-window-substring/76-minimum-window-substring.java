class Solution {
    public String minWindow(String s, String t) {
        // rolling hash
        Map<Character, Integer> rolling = new HashMap<>();
        Map<Character, Integer> target = new HashMap<>();
        int left = 0, right = 0;
        int s_len = s.length();

        this.constructMap(t, target);
        //sliding window
        int[] res = new int[]{Integer.MAX_VALUE,0,0};
        while(right < s_len){
            char cur_char = s.charAt(right++);
            int val = rolling.getOrDefault(cur_char, 0);
            rolling.put(cur_char, val + 1);
            //shrink
            while(left < right && this.compareMap(rolling, target)){
                char left_char = s.charAt(left);
                int temp = rolling.get(left_char);
                rolling.put(left_char, temp - 1);
                if (right - left < res[0]){
                    res[0] = right - left;
                    res[1] = left;
                    res[2] = right;
                }
                left++;
            }
            
        }
        return s.substring(res[1], res[2]);
        
    }
    public void constructMap(String s, Map<Character, Integer> m){
        int s_len = s.length();
        for(int i = 0; i < s_len; i++){
            char elem = s.charAt(i);
            int val = m.getOrDefault(elem, 0);
            m.put(elem, val + 1);
        }
    }
    public boolean compareMap(Map<Character, Integer> s, Map<Character, Integer> t){
        for(Map.Entry<Character, Integer> entry : t.entrySet()){
            if(!s.containsKey(entry.getKey()) || s.get(entry.getKey()) < entry.getValue())
                return false;
        }
        return true;
    }
}