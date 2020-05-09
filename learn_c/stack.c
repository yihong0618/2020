#include<stdio.h>

#define N 500
int stack[N];
int i=0;

void push(int a) {
    stack[i] = a;
    i = i + 1;
}

/* int pop(void) { */
/*     return stack[--i]; */
/* } */
int pop(void) {
    int val = stack[i-1];
    i--;
    return val;
}

int main() {
    push(3);
    push(4);
    push(5);
    push(1);
    int val = pop();
    push(8);
    pop();
    pop();
    printf("%d\n", val);
    for(int k=0;k<i;k++) {
        printf("%d", stack[k]);
    }
    printf("\n");
    printf("%d\n", i);
}

