#include <stdio.h>

int maxSubArraySum(int arr[], int size) {
    int max_so_far = arr[0], max_ending_here = arr[0];
    
    for (int i = 1; i < size; i++) {
        max_ending_here = (arr[i] > max_ending_here + arr[i]) ? arr[i] : max_ending_here + arr[i];
        max_so_far = (max_so_far > max_ending_here) ? max_so_far : max_ending_here;
    }
    
    return max_so_far;
}
