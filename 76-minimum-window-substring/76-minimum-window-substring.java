class Solution {
    public String minWindow(String s, String t) {
        // rolling hash
        HashMap<Character, Integer> windowMap = new HashMap<>();
        HashMap<Character, Integer> targetMap = new HashMap<>();
        int left = 0, right = 0;
        int N = s.length();
        int ans = Integer.MAX_VALUE;
        String res = "";
        constructMap(t, targetMap);
        while(right < N){
            char curChar = s.charAt(right);
            windowMap.computeIfAbsent(curChar, k->0);
            windowMap.put(curChar, (int) windowMap.get(curChar) + 1);
            right++;
            while(left < right && compareMap(targetMap, windowMap)){
                char leftChar = s.charAt(left);
                windowMap.put(leftChar, windowMap.get(leftChar) - 1);
                if(ans > right - left){
                ans = Math.min(ans, right - left);
                    res = s.substring(left, right);
                }
                left++;
            }
        }
        return res;
    }
    
    public void constructMap(String t, Map targetMap){
        for(int i = 0; i < t.length(); i++){
            char curChar = t.charAt(i);
            targetMap.computeIfAbsent(curChar, k -> 0);
            targetMap.put(curChar, (int) targetMap.get(curChar) + 1);   
        }
    }
    public boolean compareMap(Map<Character, Integer> targetMap, Map<Character, Integer> windowMap){
        for(Map.Entry<Character, Integer> entry : targetMap.entrySet()){
            char key = entry.getKey();
            int freq = entry.getValue();
            if(!windowMap.containsKey(key) || windowMap.get(key) < freq)return false;
        }
        return true;
    }

}