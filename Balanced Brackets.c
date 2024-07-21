#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int isBalanced(char *s) {
    int n = strlen(s), top = -1;
    char stack[n];
    
    for (int i = 0; i < n; i++) {
        if (s[i] == '(' || s[i] == '[' || s[i] == '{') {
            stack[++top] = s[i];
        } else {
            if (top == -1) return 0;
            char last = stack[top--];
            if ((s[i] == ')' && last != '(') || (s[i] == ']' && last != '[') || (s[i] == '}' && last != '{')) {
                return 0;
            }
        }
    }
    
    return top == -1;
}
