class MedianFinder {
    //two stacks
    //leftLinkedList, rightLinkedList
    //isOdd
    int count = 0;
    PriorityQueue<Integer> leftHeap;
    PriorityQueue<Integer> rightHeap;
    public MedianFinder() {
        
        leftHeap = new PriorityQueue<>((a, b) -> (b - a));
        rightHeap = new PriorityQueue<>((a, b) -> (a - b));
        
        leftHeap.add(-100001);
        rightHeap.add(100001);
        

        
    }
    
    public void addNum(int num) {
        
        count++;
        
        int leftHeapTop = leftHeap.peek();
        int rightHeapTop = rightHeap.peek();
        
       
        if (leftHeapTop >= num){
            leftHeap.add(num);
        }else{
            rightHeap.add(num);
        }
        
        
        if(leftHeap.size() - rightHeap.size() == - 1){
            int popped = rightHeap.poll();
            leftHeap.offer(popped);
        }else if(leftHeap.size() - rightHeap.size() > 1){
            int popped = leftHeap.poll();
            rightHeap.offer(popped);            
        }
    }
    

    
    public double findMedian() {
        
        int left = leftHeap.peek();
        int right = rightHeap.peek();
        
        if(count%2 == 0){
            return (left + right) / 2.0;
            
        }else{
            return left;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */