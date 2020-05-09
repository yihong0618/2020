#include<stdio.h>

void swap(int *a, int *b) {
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}


int main() {
    int a, b;
    a = 3;
    b = 4;
    swap(&a, &b);
    printf("a=%d, b=%d", a, b);
}
