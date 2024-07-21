#include <stdlib.h>

int comparator(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

void sortArray(int arr[], int n) {
    qsort(arr, n, sizeof(int), comparator);
}
