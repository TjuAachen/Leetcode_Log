class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        HashMap<Character, Integer> counter = new HashMap<>();
        int N = magazine.length();
        for(int i = 0; i < N; i++){
            char cur_char = magazine.charAt(i);
            if(counter.containsKey(cur_char)){
                
                int cur_val = counter.get(cur_char);
                counter.put(cur_char, cur_val+1);
            }else{
                counter.put(cur_char, 1);
            }
        }
        for(int j = 0; j < ransomNote.length(); j++){
            char cur_char = ransomNote.charAt(j);
            if (counter.containsKey(cur_char)){
                if (counter.get(cur_char) == 0){
                    return false;
                }
                int cur_val = counter.get(cur_char);
                counter.put(cur_char, cur_val-1);
            }else{
                return false;
            }
        }
        return true;
        
    }
}