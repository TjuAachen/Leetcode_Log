class Solution {
    public int maxSumSubmatrix(int[][] matrix, int k) {
        int nrow = matrix.length, ncol = matrix[0].length;
        int res = Integer.MIN_VALUE;
        for (int start_row = 0; start_row < nrow; start_row++){
            int[] cur_row = new int[ncol + 1];
            int[] prev_row = new int[ncol + 1];
            for(int row = start_row; row < nrow;  row++){
                TreeSet<Integer> ts = new TreeSet<>();
                for(int col = 0; col < ncol; col++){
                    cur_row[col + 1] = cur_row[col] + prev_row[col+1] - prev_row[col] +matrix[row][col];
                    ts.add(cur_row[col]);
                   // System.out.println(cur_row[col+1]);
                    int target = cur_row[col + 1] - k;
                    if (ts.ceiling(target) != null){
                        int val = ts.ceiling(target);
                        res = Math.max(cur_row[col + 1]-val, res);
                    }
                    if(res == k) return k;

                }
                prev_row = cur_row.clone();
            }
              
        }
        return res;
    }
}