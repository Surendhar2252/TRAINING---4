#include <stdio.h>
#include <stdlib.h>

long arrayManipulation(int n, int queries[][3], int q) {
    long *arr = calloc(n + 1, sizeof(long));
    long max_value = 0, current = 0;
    
    for (int i = 0; i < q; i++) {
        int a = queries[i][0], b = queries[i][1], k = queries[i][2];
        arr[a] += k;
        if (b + 1 <= n) arr[b + 1] -= k;
    }
    
    for (int i = 1; i <= n; i++) {
        current += arr[i];
        if (current > max_value) max_value = current;
    }
    
    free(arr);
    return max_value;
}
