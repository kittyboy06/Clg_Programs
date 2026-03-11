#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define SIZE 50
char stack[SIZE];
int top = -1;
void push(char c){ stack[++top] = c; }
char pop(){ return stack[top--]; }
char peek(){ return top==-1 ? '\0' : stack[top]; }
int prec(char c){
    if(c=='^') return 3;
    if(c=='*'||c=='/') return 2;
    if(c=='+'||c=='-') return 1;
    return 0;
}
void infixToPostfix(char* exp){
    char postfix[SIZE]; int k=0;
    for(int i=0; exp[i]; i++){
        char c = exp[i];
        if(isalnum(c)) postfix[k++] = c;
        else if(c=='(') push(c);
        else if(c==')'){
            while(peek()!='(') postfix[k++] = pop();
            pop();
        } else {
            while(top!=-1 && prec(peek())>=prec(c)) postfix[k++] = pop();
            push(c);
        }
    }
    while(top!=-1) postfix[k++] = pop();
    postfix[k] = '\0';
    printf("Postfix: %s\n", postfix);
}
int main(){
    char exp[50];
    printf("Enter infix expression: ");
    scanf("%s", exp);
    infixToPostfix(exp);
    return 0;
}
