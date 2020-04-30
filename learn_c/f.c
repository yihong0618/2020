#include<stdio.h>
#include<time.h>

int fa(int);

int main() {
    while (1){
        clock_t start = clock();
        int b;
        scanf("%d", &b);
        b = fa(b);
        clock_t end = clock();
        printf("%d\n", b);
        double d = (double)(end-start) / CLOCKS_PER_SEC;
        printf("%f\n", d);
    }
}
int fa(int a) {
    if (a <= 2) {
        return 1;
    }
    return fa(a-1) + fa(a-2);
}
