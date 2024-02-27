#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *create_dyn_array(int n)  {
    int *array = malloc(n*sizeof(int));
    for (int i = 0; i < n; i++) {
        scanf("%d", &array[i]);
    }
    return array;
}

int *add_dyn_array(int *arr, int num, int newval) {
    int *new_array = realloc(arr, (num+1)*sizeof(int));
    new_array[num] = newval;
    return new_array;
}
