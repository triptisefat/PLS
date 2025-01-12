#include <stdio.h>
#include <stdlib.h>

int main() {
    // Pointer declaration
    int *ptr;
    // Dynamic memory allocation
    ptr = (int *)malloc(sizeof(int));
    
    if (ptr == NULL) {
        printf("Memory allocation failed\n");
        return 1;
    }

    // Assigning value to allocated memory
    *ptr = 42;
    printf("Value pointed by ptr: %d\n", *ptr);

    // Freeing allocated memory
    free(ptr);
    return 0;
}
