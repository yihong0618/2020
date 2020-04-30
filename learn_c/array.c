#include<stdio.h>
#include<stdlib.h>
#define N 20

int a[N];

void gen_random(int upper) {
    for(int i=0; i< N; i++) {
        a[i] = rand() % upper;
    }
}

void print_rand() {
    for(int i=0; i<N;i++) {
        printf("%d ", a[i]);
    }
}

int main() {
    gen_random(10);
    print_rand();
}
