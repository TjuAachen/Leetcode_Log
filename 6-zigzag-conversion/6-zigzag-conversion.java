class Solution {
    public String convert(String s, int numRows) {
        HashMap <Integer, ArrayList<Character>> res_map= new HashMap<Integer, ArrayList<Character>>();
        int N = s.length();
        int row = 0;
        boolean ticket = true;
        for (int i = 0; i < N; i++){
            char cur_char = s.charAt(i);
            if (res_map.get(row) == null) {
            res_map.put(row, new ArrayList<Character>());
            }
            res_map.get(row).add(cur_char);
            if (ticket){
                row++;
            }else{
                row--;
            }
            if(ticket && row == numRows - 1){
                ticket = false;
            }
            if(!ticket && row == 0){
                ticket = true;
            }
        }
        StringBuilder res = new StringBuilder();
        for (Integer i : res_map.keySet()){
            List<Character> temp = res_map.get(i);
            for (int j = 0; j < temp.size(); j ++){
                res.append(temp.get(j));
            }
        }
        return res.toString();
    }
}