#include<stdio.h>


int a[] = {10, 5, 2, 4, 7, 9, 11};

void insert_sort(void) {
    int size;
    size = sizeof(a)/sizeof(int);
    int i, j, key;
    for(int j=1; j < size; j++) {
        key = a[j];
        i = j - 1;
        while (i>=0 && a[i] > key) {
            a[i+1] = a[i];
            i--;
        }
        a[i+1] = key;
    }
}

int main() {
    insert_sort();
    printf("%d,%d,%d,%d,%d,%d,%d\n", a[0], a[1], a[2], a[3], a[4], a[5], a[6]);
}
