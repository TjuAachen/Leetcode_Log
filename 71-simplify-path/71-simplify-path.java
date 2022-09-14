class Solution {
    public String simplifyPath(String path) {
        //1. remove multiple slash to a single slash
        
        //2. remove trailing / 
        
        //3. set one period as the current directory
        
        //4. set two period up
        LinkedList<String> canonicalPath = new LinkedList<>();
        for(int i = 0; i < path.length();){
            char curChar = path.charAt(i);
            if(curChar == '/'){
                int j = i;
                while(j < path.length() && path.charAt(j) == '/'){
                    j++;
                }
                if(j != path.length()){
                    if(canonicalPath.size() == 0||!canonicalPath.peekLast().equals("/"))canonicalPath.addLast("/");
                }
                i = j;
            
            }else{
                i = handleDirectory(path, i, canonicalPath);   
            }   
        }
        
        return ListToString(canonicalPath);
        
    }
    //return new i
    //handle directory
    public String ListToString(LinkedList<String> res){
        StringBuilder ans = new StringBuilder();
        //remove trailing
        while(res.size() > 1 && res.peekLast().equals("/")){
            res.pollLast();
        }
        for(String e : res){
            ans.append(e);
        }
        if(res.size() == 0)return "/";
        return ans.toString();
        
        
    }
    
    
    public int handleDirectory(String path, int start, LinkedList res){
        int i = start;
        StringBuilder temp = new StringBuilder();
        while(i < path.length() && path.charAt(i) != '/'){
            temp.append(path.charAt(i++));
        }
        String tempRes = temp.toString();
        if(tempRes.equals("..")){
            if(res.size() > 2){
                res.pollLast();
                res.pollLast();
                res.pollLast();
            }
            
        }else if(tempRes.equals(".")){
            return i+1;
        }else{
            res.addLast(tempRes);
        }
        return i;
    }
    
}