class Solution {
    public boolean validUtf8(int[] data) {
        int i = 0;
        int N = data.length;
        


        int eight = 0, seven = 0, six = 0, five = 0,four = 0;
        while(i < N){
            int curNum = data[i];
            int followingNums = -1;
            eight = curNum&(1<<7);
            seven = curNum&(1<<6);
            six = curNum&(1<<5);
            five = curNum&(1<<4);
            four = curNum&(1<<3);
            //first case
            if(eight == 0){
                followingNums = 0;
            }else if(seven != 0 && six == 0){
                followingNums = 1;
            }else if(seven != 0 && six != 0 && five == 0){
                followingNums = 2;
            }else if(seven != 0 && six != 0 && five != 0 && four == 0){
                followingNums = 3;
            }
            if(followingNums == -1)return false;
            if(followingNums == 0){
                i++;
                continue;
            }
            i++;
            while(followingNums > 0){
                if(i >= data.length)return false;
                int nxtNum = data[i];
                eight = nxtNum&(1<<7);
                seven = nxtNum&(1<<6);
                if(eight == 0 || seven != 0)return false;
                i++;
                followingNums--;
            }
        
    }
        return true;
    }
}