int removeDuplicates(int* nums, int numsSize){
    
    int boundary = 0;
    
    for (int i = 0; i < numsSize; ++i){
        int curNum = nums[i];
        if(boundary == 0 || curNum != nums[boundary - 1]){
            nums[boundary] = curNum;
            boundary++;
        }
    }
    
    return boundary;
    
}