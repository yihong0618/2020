#include<stdio.h>

int a[] = {2, 3, 1, 4, 5, 44, 9};
int L = sizeof(a)/sizeof(int);

void sort(void) {
    for(int j=1; j<L; j++) {
        int key = a[j];
        int i = j-1;
        while (i>=0 && a[i]>key) {
            a[i+1] = a[i];
            i--;
        }
        a[i+1] = key;
    }
    
}

int main() {
    sort();
    for(int i=0; i< L; i++) {
        printf("%d \n", a[i]);
    }
}
