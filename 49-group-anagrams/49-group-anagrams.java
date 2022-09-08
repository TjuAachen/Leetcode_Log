class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> mapRes = new HashMap<>();
        List<List<String>> res = new LinkedList<>();
        
        for(String str : strs){
            char[] temp = str.toCharArray();
            Arrays.sort(temp);
            String sorted = String.valueOf(temp);
            mapRes.computeIfAbsent(sorted, k -> new LinkedList());
            mapRes.get(sorted).add(str);
        }
        
        for(Map.Entry<String, List<String>> entry : mapRes.entrySet()){
            res.add(entry.getValue());
        }
        return res;
    }
}