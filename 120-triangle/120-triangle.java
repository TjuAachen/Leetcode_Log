class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        List<Integer> prevRow = triangle.get(0);
        for(int row = 1; row < triangle.size(); row++){
            List<Integer> curRow = new ArrayList<>();
            for(int col = 0; col <= row; col++){
                int smallestAbove = Integer.MAX_VALUE;
                if(col > 0){
                    smallestAbove = prevRow.get(col - 1);
                }
                if(col < row){
                    smallestAbove = Math.min(smallestAbove, prevRow.get(col));
                }
                curRow.add(smallestAbove + triangle.get(row).get(col));
            }
            prevRow = curRow;
        }
        return Collections.min(prevRow);
    }
}