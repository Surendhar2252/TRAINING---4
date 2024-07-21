#include <stdio.h>
#include <stdlib.h>

typedef struct {
    int *array;
    int size;
    int capacity;
} DynamicArray;

DynamicArray* createArray(int capacity) {
    DynamicArray *arr = malloc(sizeof(DynamicArray));
    arr->array = malloc(capacity * sizeof(int));
    arr->size = 0;
    arr->capacity = capacity;
    return arr;
}

void insert(DynamicArray *arr, int element) {
    if (arr->size == arr->capacity) {
        arr->capacity *= 2;
        arr->array = realloc(arr->array, arr->capacity * sizeof(int));
    }
    arr->array[arr->size++] = element;
}
