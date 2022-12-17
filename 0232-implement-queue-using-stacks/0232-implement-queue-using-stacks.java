class MyQueue {
    
    LinkedList<Integer> inStack;
    LinkedList<Integer> outStack;
    
    public MyQueue() {
        inStack = new LinkedList<>();
        outStack = new LinkedList<>();
        
        
    }
    
    public void push(int x) {
        inStack.addLast(x);
    }
    
    public int pop() {
        if (!outStack.isEmpty()){
            return outStack.pollLast();
        }else{
            while(!inStack.isEmpty()){
                outStack.addLast(inStack.pollLast());
            }
        }
        
        if (outStack.isEmpty())
            return -1;
        return outStack.pollLast();
    }
    
    public int peek() {
        if (!outStack.isEmpty()){
            return outStack.getLast();
        }else{
            while(!inStack.isEmpty()){
                    outStack.addLast(inStack.pollLast());
            }            
        }

        if (outStack.isEmpty())
            return -1;
        return outStack.getLast();
        
    }
    
    public boolean empty() {
        if (inStack.isEmpty() && outStack.isEmpty())
            return true;
        return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */