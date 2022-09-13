class Solution {
    public boolean validUtf8(int[] data) {
        int N = data.length;
        int numOfBytesToProcess = 0;
        
        int mask1 = 1<<7, mask2 = 1<<6;
        
        for(int i = 0; i < data.length; i++){
            if(numOfBytesToProcess == 0){
                int mask = 1<<7;
                while((mask & data[i]) != 0){
                    numOfBytesToProcess += 1;
                    mask = mask>>1;
                }
                if(numOfBytesToProcess == 0)continue;
                if(numOfBytesToProcess > 4 || numOfBytesToProcess == 1)return false;
            }else{
                if ((data[i] & mask1) == 0 || (data[i] & mask2) != 0)return false;
            }
            numOfBytesToProcess--;
        
            
        }
        return numOfBytesToProcess == 0;


    }
}