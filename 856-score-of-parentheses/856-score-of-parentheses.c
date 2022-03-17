#include <stdio.h>
#include <string.h>
int scoreOfParentheses(char * s){
    int* stack = (int*) malloc(sizeof(int)*strlen(s));
    int res = 0;
    int j = 0;
    
    for(int i = 0;i < strlen(s); i++ ){
        if (s[i] == '('){
            
            stack[j] = res; 
            j = j + 1;
            res = 0;
        }else{
            
            if(res*2 > 1){
            res = stack[j-1] + 2*res;
                }else{
                res = stack[j-1] + 1;
            }
            j = j - 1;
        }
    }
 return res;
}