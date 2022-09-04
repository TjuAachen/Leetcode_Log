class Solution {
    public boolean isRectangleCover(int[][] rectangles) {
        //每次加入一个矩形，即更新高度
        //preprocess
        int N = rectangles.length;
        int[][] data = new int[2*N][4];
        int idx = 0;
        for(int[] rectangle : rectangles){
        int x1 = rectangle[0];int y1 = rectangle[1];int x2 = rectangle[2];int y2 = rectangle[3];
        //1 - left
        data[idx++] = new int[]{x1, y1, y2, 1};
        data[idx++] = new int[]{x2, y1, y2, 0};
        
        }
        Arrays.sort(data , (o1,o2)-> o1[0]!=o2[0]?o1[0]-o2[0]:o1[1]-o2[1]);
        //按顶点处理,边缘特殊考虑
        int i = 0;
        
        while(i < 2 * N){
            //extract the same point and separate by the flag pos
            List<int[]> left = new ArrayList<>();
            List<int[]> right = new ArrayList<>();
            int cur_x = data[i][0];
            int j = i;
            while(j < 2*N && data[j][0] == cur_x){
                List<int[]> list = data[j][3] == 1?left:right;
                int[] cur = new int[]{data[j][1], data[j][2]};
                if(list.isEmpty()){
                     list.add(cur);
                }else{
                    int[] prev = list.get(list.size() - 1);
                    //if overlapping
                    if(prev[1] > cur[0]) return false;
                    if(prev[1] == cur[0])prev[1] = cur[1];
                    if(prev[1] < cur[0]) list.add(cur);
                }
                j++;
            }
            //middle
           // System.out.printf("%d %d %d %d\n",i, j,left.size(), right.size());
            if(i > 0 && j < 2*N){
                if(left.size() != right.size()) return false;
                for(int k = 0; k < left.size(); k++){
                    if(left.get(k)[0] != right.get(k)[0] || left.get(k)[1] != right.get(k)[1])return false;
                }
            }else if (left.size() + right.size() != 1) {return false;
            }
            i = j;         
        }        
        return true;
    }

}