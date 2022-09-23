class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> prev = new LinkedList<>(Arrays.asList(1));
        if(rowIndex == 0)return prev;
        for(int i = 1; i <= rowIndex; i++){
            List<Integer> temp = new LinkedList<>();
            temp.add(1);
            for(int j = 0; j < prev.size() - 1; j++){
                temp.add(prev.get(j) + prev.get(j+1));
            }
            temp.add(1);
            prev = temp;
        }
        return prev;
        
        
    }
}